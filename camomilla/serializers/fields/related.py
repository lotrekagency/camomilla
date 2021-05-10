from collections import OrderedDict
from rest_framework import serializers


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
            kwargs["queryset"] = kwargs.get(
                "queryset", self.serializer.Meta.model.objects.all()
            )
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

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}
        if cutoff is not None:
            queryset = queryset[:cutoff]

        return OrderedDict(
            [
                (
                    super(RelatedField, self).to_representation(item),
                    self.display_value(item),
                )
                for item in queryset
            ]
        )
