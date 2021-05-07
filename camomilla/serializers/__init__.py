from rest_framework import serializers
from ..models import Article, Tag, Category, Content, Media, Page, MediaFolder

from hvad.contrib.restframework import TranslatableModelSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db import IntegrityError

from django.utils.translation import ugettext_lazy as _

from rest_framework.validators import ValidationError
from rest_framework.response import Response
from hvad.contrib.restframework import TranslationsMixin
from django.conf import settings


class RelatedField(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop("serializer", None)
        self.lookup = kwargs.pop("lookup", "id")
        if self.serializer is not None:
            assert issubclass(
                self.serializer, serializers.Serializer
            ), '"serializer" is not a valid serializer class'
            assert hasattr(
                self.serializer.Meta, "model"
            ), 'Class {serializer_class} missing "Meta.model" attribute'.format(
                serializer_class=self.serializer.__class__.__name__
            )
            kwargs["queryset"] = kwargs.get("queryset", self.serializer.Meta.model.objects.all()) 
            # kwargs["allow_null"] = kwargs.get("allow_null", self.serializer.Meta.model._meta.get_field(self.source).null)
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)
    
    def to_internal_value(self, data):
        if isinstance(data, dict):
            return self.get_queryset().get(**{self.lookup: data.get(self.lookup, None)})
        return super().to_internal_value(data)


class CamomillaBaseTranslatableModelSerializer(TranslatableModelSerializer):
    translated_languages = serializers.SerializerMethodField(
        "get_available_translations", read_only=True
    )
    active_languages = serializers.SerializerMethodField(
        "get_active_languages", read_only=True
    )

    def get_available_translations(self, obj):
        return obj.get_available_languages()

    def get_active_languages(self, request, *args, **kwargs):
        languages = []
        for key, language in settings.LANGUAGES:
            languages.append({"id": key, "name": language})
        return {"active": settings.LANGUAGE_CODE, "languages": languages}


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):

    user_permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    repassword = serializers.CharField(
        write_only=True, required=False, allow_null=True, allow_blank=True
    )
    level = serializers.CharField(required=False)
    has_token = serializers.SerializerMethodField("get_token", read_only=True)
    user_permissions = PermissionSerializer(read_only=True, many=True)

    def get_token(self, obj):
        try:
            obj.auth_token
            return True
        except:
            return False

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "repassword",
            "level",
            "user_permissions",
            "has_token",
            "is_superuser",
        )

    def validate(self, data):
        new_password = data.get("password", "")
        if new_password and len(new_password) < 8:
            raise serializers.ValidationError(_("Passwords too short"))
        if new_password != data.get("repassword", ""):
            raise serializers.ValidationError(_("Passwords should match"))
        return data

    def create(self, validated_data):
        user = get_user_model()(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            level=validated_data["level"],
        )
        if validated_data.get("password", ""):
            user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.level = validated_data.get("level", instance.level)
        if validated_data.get("password", ""):
            instance.set_password(validated_data["password"])
        permissions = validated_data.get("user_permissions", [])
        instance.user_permissions.clear()
        for permission in permissions:
            instance.user_permissions.add(permission)
        instance.save()
        return instance


class TagSerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    def create(self, validated_data):
        try:
            return super(TagSerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError({"title": ["Esiste già un Tag con questo titolo"]})

    def update(self, instance, data):
        try:
            return super(TagSerializer, self).update(instance, data)
        except IntegrityError:
            return Response({"title": ["Esiste già un Tag con questo titolo"]})

    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    def create(self, validated_data):
        try:
            return super(CategorySerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError(
                {"title": ["Esiste già una Categoria con questo titolo"]}
            )

    def update(self, instance, data):
        try:
            return super(CategorySerializer, self).update(instance, data)
        except IntegrityError:
            raise ValidationError(
                {"title": ["Esiste già una Categoria con questo titolo"]}
            )

    class Meta:
        model = Category
        fields = "__all__"


class UnderTranslateMixin(object):
    def __init__(self, *args, **kwargs):
        self.ulanguage = "en"
        try:
            self.ulanguage = kwargs.pop("ulanguage")
        except KeyError:
            pass
        super(UnderTranslateMixin, self).__init__(*args, **kwargs)


class ContentSerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    def create(self, validated_data):
        try:
            return super(ContentSerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError(
                {"identifier": ["Esiste già un contenuto con questo identifier"]}
            )

    def update(self, instance, data):
        try:
            return super(ContentSerializer, self).update(instance, data)
        except IntegrityError:
            return Response(
                {"identifier": ["Esiste già un contenuto con questo identifier"]}
            )

    class Meta:
        model = Content
        fields = "__all__"


class MediaSerializer(CamomillaBaseTranslatableModelSerializer):
    def exclude_fields(self, fields_to_exclude=None):
        if isinstance(fields_to_exclude, list):
            for f in fields_to_exclude:
                f in self.fields.fields and self.fields.fields.pop(f) or next()

    class Meta:
        model = Media
        fields = "__all__"


class MediaDetailSerializer(CamomillaBaseTranslatableModelSerializer):
    links = serializers.SerializerMethodField("get_linked_instances")

    class Meta:
        model = Media
        fields = "__all__"

    def get_linked_instances(self, obj):
        result = []
        links = obj.get_foreign_fields()
        for link in links:
            objects = getattr(obj, link).all()
            for item in objects:
                if item.__class__.__name__ != "MediaTranslation":
                    result.append(
                        {
                            "model": item.__class__.__name__,
                            "name": item.__str__(),
                            "id": item.pk,
                        }
                    )
        return result


class MediaFolderSerializer(CamomillaBaseTranslatableModelSerializer):
    icon = MediaSerializer(read_only=True)

    class Meta:
        model = MediaFolder
        fields = "__all__"


class ArticleSerializer(
    TranslationsMixin, UnderTranslateMixin, CamomillaBaseTranslatableModelSerializer
):

    highlight_image = RelatedField(serializer=MediaSerializer, allow_null=True)
    tags = RelatedField(serializer=TagSerializer, many=True, allow_null=True)
    og_image = RelatedField(serializer=MediaSerializer, allow_null=True)

    def create(self, validated_data):
        try:
            return super(ArticleSerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError(
                {"permalink": ["Esiste già un articolo con questo permalink"]}
            )

    def update(self, instance, data):
        try:
            return super(ArticleSerializer, self).update(instance, data)
        except IntegrityError:
            return Response(
                {"permalink": ["Esiste già un articolo con questo permalink"]}
            )

    class Meta:
        model = Article
        fields = "__all__"


class ExpandedArticleSerializer(
    TranslationsMixin, UnderTranslateMixin, CamomillaBaseTranslatableModelSerializer
):

    tags = serializers.SerializerMethodField("get_translated_tags")
    categories = serializers.SerializerMethodField("get_translated_categories")
    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source="highlight_image", read_only=True)
    og_image_exp = MediaSerializer(source="og_image", read_only=True)

    def create(self, validated_data):
        try:
            return super(ExpandedArticleSerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError(
                {"permalink": ["Esiste già un articolo con questo permalink"]}
            )

    def update(self, instance, data):
        try:
            return super(ExpandedArticleSerializer, self).update(instance, data)
        except IntegrityError:
            return Response(
                {"permalink": ["Esiste già un articolo con questo permalink"]}
            )

    class Meta:
        model = Article
        fields = "__all__"

    def get_translated_tags(self, obj):
        tags = (
            Tag.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        )
        return TagSerializer(tags, many=True).data

    def get_translated_categories(self, obj):
        categories = (
            Category.objects.language(self.ulanguage)
            .fallbacks()
            .filter(article__pk=obj.pk)
        )
        return CategorySerializer(categories, many=True).data


class PageSerializer(
    TranslationsMixin, UnderTranslateMixin, CamomillaBaseTranslatableModelSerializer
):
    og_image_exp = MediaSerializer(source="og_image", read_only=True)
    content_set = serializers.SerializerMethodField("get_translated_content")

    class Meta:
        model = Page
        fields = "__all__"

    def get_translated_content(self, obj):
        content = (
            Content.objects.language(self.ulanguage).fallbacks().filter(page__pk=obj.pk)
        )
        return ContentSerializer(content, many=True).data


class CompactPageSerializer(
    TranslationsMixin, CamomillaBaseTranslatableModelSerializer
):
    class Meta:
        model = Page
        fields = ("id", "identifier", "title", "description", "permalink", "og_image")
