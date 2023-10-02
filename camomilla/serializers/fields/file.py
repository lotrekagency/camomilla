from rest_framework.fields import FileField as DRFFileField
from rest_framework.fields import ImageField as DRFImageField
from rest_framework.fields import Field


class SafeFileFieldMixin(Field):
    """
    This mixin prevents errors when trying to upload a file passing its current url.
    In such cases, the current file will be kept.
    """

    def to_internal_value(self, data):
        current = getattr(self.parent.instance, self.field_name, None)
        if (
            isinstance(data, str)
            and current
            and data.endswith(getattr(current, "url", ""))
        ):
            return current
        return super().to_internal_value(data)


class FileField(SafeFileFieldMixin, DRFFileField):
    pass


class ImageField(SafeFileFieldMixin, DRFImageField):
    pass
