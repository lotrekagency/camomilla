import traceback
from io import BytesIO

from django.core.files.base import ContentFile
from django.core.files.storage import get_storage_class
from PIL import Image

from camomilla import settings


class OptimizedStorage(get_storage_class()):
    MEDIA_MAX_WIDTH = settings.MEDIA_OPTIMIZE_MAX_WIDTH
    MEDIA_MAX_HEIGHT = settings.MEDIA_OPTIMIZE_MAX_HEIGHT
    MEDIA_DPI = settings.MEDIA_OPTIMIZE_DPI

    def __init__(self, *args, **kwargs) -> None:
        self.MEDIA_MAX_WIDTH = kwargs.pop("max_width", self.MEDIA_MAX_WIDTH)
        self.MEDIA_MAX_HEIGHT = kwargs.pop("max_height", self.MEDIA_MAX_HEIGHT)
        self.MEDIA_DPI = kwargs.pop("dpi", self.MEDIA_DPI)
        super().__init__(*args, **kwargs)

    def _save(self, name, content):
        if settings.ENABLE_MEDIA_OPTIMIZATION:
            content, _ = self._optimize(name, content)
        return super(OptimizedStorage, self)._save(name, content)

    def _optimize(self, name, content):
        try:
            image = Image.open(content)
            width, height = image.size
            if width <= height:
                selected_width = int((self.MEDIA_MAX_HEIGHT / height) * width)
                selected_height = self.MEDIA_MAX_HEIGHT
            else:
                selected_height = int((self.MEDIA_MAX_WIDTH / width) * height)
                selected_width = self.MEDIA_MAX_WIDTH

            image = image.resize(
                [selected_width, selected_height], resample=Image.LANCZOS
            )
            image.info["dpi"] = (self.MEDIA_DPI, self.MEDIA_DPI)
            tmp = BytesIO()
            ext = name.split(".")[-1].lower().replace("jpg", "jpeg")
            image.save(tmp, ext, dpi=(self.MEDIA_DPI, self.MEDIA_DPI), optimize=True)
            tmp.seek(0)
            optimized_content = ContentFile(tmp.read())
            tmp.close()
            content.close()
            return optimized_content, True
        except Exception:
            traceback.print_exc()
            return content, False
