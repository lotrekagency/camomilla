from rest_framework.fields import FileField as DRFFileField
from rest_framework.fields import ImageField as DRFImageField


class FileField(DRFFileField):
    def to_internal_value(self, data):
        current = getattr(self.parent.instance, self.field_name, None)
        if (
            isinstance(data, str)
            and current
            and data.endswith(getattr(current, "url", ""))
        ):
            return getattr(current, "name", "")
        return super().to_internal_value(data)


class ImageField(DRFImageField):
    def to_internal_value(self, data):
        current = getattr(self.parent.instance, self.field_name, None)
        if (
            isinstance(data, str)
            and current
            and data.endswith(getattr(current, "url", ""))
        ):
            return getattr(current, "name", "")
        return super().to_internal_value(data)
