from collections import defaultdict
from functools import cached_property

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from camomilla.models import Media, UrlNode
from camomilla.serializers.fields import RelatedField
from camomilla.serializers.media import MediaSerializer as FullMediaSerializer
from camomilla.utils.getters import pointed_getter


class MinifiedJSONField(serializers.Serializer):
    def to_internal_value(self, data):
        return {
            k: [vv.pk for vv in v if vv]
            if isinstance(self.fields[k], serializers.ManyRelatedField)
            else (
                v and v.pk
                if isinstance(self.fields[k], serializers.RelatedField)
                else v
            )
            for k, v in super().to_internal_value(data).items()
        }

    def get_all_relateds(self, instance):
        relateds = defaultdict(set)
        options = {
            "prefetch_related": defaultdict(set),
            "select_related": defaultdict(set),
        }
        if instance and type(instance) == dict:
            for k, v in instance.items():
                if not k in self.fields:
                    continue
                field = self.fields[k]
                related_field = getattr(field, "child_relation", field)
                model = pointed_getter(
                    related_field, "serializer.Meta.model"
                ) or pointed_getter(related_field, "queryset.model")
                if isinstance(related_field, RelatedField):
                    serializer = getattr(related_field, "serializer", None)
                    if serializer:
                        for f in serializer().fields.values():
                            if isinstance(f, serializers.ManyRelatedField):
                                options["prefetch_related"][model].add(f.source)
                            elif isinstance(f, serializers.RelatedField):
                                options["select_related"][model].add(f.source)

                if isinstance(field, serializers.ManyRelatedField):
                    relateds[model].update([i for i in v if i])
                elif isinstance(field, serializers.RelatedField):
                    relateds[model].add(v)
                elif isinstance(getattr(field, "child", field), MinifiedJSONField):
                    values = (
                        [instance.get(k)]
                        if type(instance.get(k)) != list
                        else instance.get(k)
                    )
                    for value in values:
                        child_relateds, child_options = getattr(
                            field, "child", field
                        ).get_all_relateds(value)
                        for model, pks in child_relateds.items():
                            relateds[model].update(pks)
                        for model, opts in child_options["select_related"].items():
                            options["select_related"][model].update(opts)
                        for model, opts in child_options["prefetch_related"].items():
                            options["prefetch_related"][model].update(opts)
        return relateds, options

    def prefetch_related(self, instance):
        if self.json_field_root != self:
            return self.json_field_root._prefetched_data
        elif not hasattr(self, "_prefetched_data"):
            relateds, options = self.get_all_relateds(instance)
            self._prefetched_data = {}
            for model, pks in relateds.items():
                qs = model.objects
                if len(options["select_related"].get(model) or []) > 0:
                    qs = qs.select_related(*options["select_related"][model])
                if len(options["prefetch_related"].get(model) or []) > 0:
                    qs = qs.prefetch_related(*options["prefetch_related"][model])
                self._prefetched_data[model] = (
                    {obj.pk: obj for obj in qs.filter(id__in=pks).all()}
                    if len(pks) > 0
                    else {}
                )
        return self._prefetched_data

    def to_representation(self, instance):
        rep = {}
        prefetched_data = self.prefetch_related(instance) or {}
        for k, v in instance.items():
            if not k in self.fields:
                continue
            field = self.fields[k]
            related_field = getattr(field, "child_relation", field)
            model = pointed_getter(
                related_field, "serializer.Meta.model"
            ) or pointed_getter(related_field, "queryset.model")
            if isinstance(field, serializers.ManyRelatedField):
                data = prefetched_data.get(model)
                rep[k] = [data[i] for i in v if i in data] if data else []
            elif isinstance(field, serializers.RelatedField):
                rep[k] = prefetched_data.get(model, {}).get(v)
            else:
                rep[k] = v
        return super().to_representation(rep)

    def get_fields(self):
        fields = super().get_fields()
        for f in fields:
            fields[f].required = False
            fields[f].allow_blank = True
            fields[f].allow_null = True
            if isinstance(fields[f], serializers.ManyRelatedField) or isinstance(
                fields[f], serializers.ListField
            ):
                fields[f].default = []
        return fields

    @cached_property
    def json_field_root(self):
        root = self
        while isinstance(root.parent, MinifiedJSONField) or (
            isinstance(root.parent, serializers.ListField)
            and isinstance(root.parent.parent, MinifiedJSONField)
        ):
            root = root.parent
        return root


class MediaSerializer(FullMediaSerializer):
    links = None
    is_image = None
    ratio = serializers.SerializerMethodField()

    def get_ratio(self, instance):
        width = instance.image_props.get("width")
        height = instance.image_props.get("height")
        if width and height:
            return width / height
        return None

    class Meta(FullMediaSerializer.Meta):
        fields = [
            "id",
            "alt_text",
            "title",
            "description",
            "file",
            "thumbnail",
            "mime_type",
            "size",
            "ratio",
        ]


class VideoField(MinifiedJSONField):
    video = RelatedField(
        serializer=MediaSerializer,
        queryset=Media.objects.filter(mime_type__startswith="video/"),
    )
    preview = RelatedField(
        serializer=MediaSerializer,
        queryset=Media.objects.filter(mime_type__startswith="video/"),
    )


class DocumentField(MinifiedJSONField):
    media = RelatedField(serializer=MediaSerializer, queryset=Media.objects.all())
    script = serializers.CharField()


class CTAField(MinifiedJSONField):
    class Relational(MinifiedJSONField):

        content_type = serializers.PrimaryKeyRelatedField(
            queryset=ContentType.objects.all()
        )
        page_id = serializers.IntegerField()
        url_node = serializers.PrimaryKeyRelatedField(queryset=UrlNode.objects.all())

    link_type = serializers.ChoiceField(
        (
            (None, "None"),
            (
                "RE",
                "Relational",
            ),
            ("ST", "Static"),
        )
    )
    relational = Relational()
    static = serializers.CharField()

    def validate(self, data):
        if self.context.get("request") and data.get("static"):
            data["static"] = data["static"].removeprefix(
                self.context.get("request").build_absolute_uri("/")[:-1]
            )
        return data

    def to_internal_value(self, data):
        ct_id = pointed_getter(data, "relational.content_type")
        p_id = pointed_getter(data, "relational.page_id")
        if (
            data.get("link_type") == "RE"
            and p_id
            and ct_id
            and not pointed_getter(data, "relational.url_node")
        ):
            c_type = ContentType.objects.filter(pk=ct_id).first()
            model = c_type and c_type.model_class()
            page = model and model.objects.filter(pk=p_id).first()
            if page:
                data["relational"]["url_node"] = page.url_node.pk
        return super().to_internal_value(data)

    def to_representation(self, instance):
        related_data = self.prefetch_related(instance)
        data = super().to_representation(instance)
        if data["link_type"] == "ST":
            data["computed"] = data["static"]
        elif data["link_type"] == "RE":
            rel = data["relational"]
            if rel.get("url_node"):
                data["computed"] = related_data[UrlNode][rel["url_node"]].permalink
            elif rel.get("content_type") and rel.get("page_id"):
                c_type = related_data[ContentType][rel["content_type"]]
                model = c_type and c_type.model_class()
                page = model and model.objects.filter(pk=rel.get("page_id")).first()
                data["computed"] = getattr(page, "permalink", None)
            data["computed"] = data.get("computed") or ""

        return data


class FullCTAField(MinifiedJSONField):
    title = serializers.CharField()
    link = CTAField()


class MultimediaField(MinifiedJSONField):
    type = serializers.ChoiceField(
        (
            (
                None,
                "Empty",
            ),
            (
                "image",
                "Image",
            ),
            (
                "video",
                "Video",
            ),
            (
                "carousel",
                "Carousel",
            ),
        )
    )
    image = RelatedField(serializer=MediaSerializer, queryset=Media.objects.all())
    video = VideoField()
    carousel = RelatedField(
        serializer=MediaSerializer, queryset=Media.objects.all(), many=True
    )
