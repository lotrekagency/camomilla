from camomilla.models import Menu
from camomilla.serializers.base import BaseModelSerializer


class MenuSerializer(BaseModelSerializer):
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
