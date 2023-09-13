import functools
from django.utils.translation import activate
from django.conf import settings


def active_lang(*args, **kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if len(args) and hasattr(args[0], "request"):
                request = args[0].request
            else:
                request = args[0] if len(args) else kwargs.get("request", None)
            lang = settings.LANGUAGE_CODE
            if request and hasattr(request, "GET"):
                lang = request.GET.get("lang", request.GET.get("language", lang))
            if request and hasattr(request, "data"):
                lang = request.data.pop("lang", request.data.pop("language", lang))
            if lang and lang in [lng[0] for lng in settings.LANGUAGES]:
                activate(lang)
                request.LANGUAGE_CODE = lang
            return func(*args, **kwargs)

        return wrapped_func

    return decorator
