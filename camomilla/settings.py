from django.conf import settings

DEFAULT_MODELS = {
    "article": "camomilla.Article",
    "category": "camomilla.Category",
    "content": "camomilla.Content",
    "page": "camomilla.Page",
    "tag": "camomilla.Tag",
    "media_folder": "camomilla.MediaFolder",
    "media": "camomilla.Media",
    **getattr(settings, "CAMOMILLA_DEFAULT_MODELS", {}),
}
