from rest_framework import serializers

from camomilla.models import Menu
from camomilla.serializers.base import BaseModelSerializer
from camomilla.serializers.fields.json import CTAField, MinifiedJSONField


class ListMenuSerializer(BaseModelSerializer):
    class Meta:
        model = Menu
        exclude = ("nodes",)


class MenuSerializer(BaseModelSerializer):
    class NodeSerializer(MinifiedJSONField):
        link = CTAField()
        title = serializers.CharField(required=True)
        meta = serializers.JSONField(default=dict)
        id = serializers.CharField()

        def get_fields(self):
            return {**super().get_fields(), "nodes": self.__class__(many=True)}

    nodes = NodeSerializer(many=True)

    def get_default_field_names(self, *args):
        field_names = super().get_default_field_names(*args)
        self.action = getattr(
            self, "action", self.context and self.context.get("action", "list")
        )
        if self.action == "list":
            return [f for f in field_names if f != "nodes"]
        return field_names

    class Meta:
        model = Menu
        fields = "__all__"
