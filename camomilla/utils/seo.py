import urllib.parse

from django.apps import apps
from django.conf import settings
from django.http import Http404
from django.urls import resolve, reverse
from django.utils.translation import activate, get_language

from camomilla.exceptions import NeedARedirect


def is_page(model):
    from camomilla.models import AbstractPage

    return next(
        (True for base in model.__bases__ if issubclass(base, AbstractPage)), False
    )


def get_host_url(request):
    if request:
        return "{0}://{1}".format(request.scheme, request.META["HTTP_HOST"])


def get_complete_url(request, url, language=""):
    prefix = getattr(settings, "PREFIX_DEFAULT_LANGUAGE", False)
    if language == settings.LANGUAGE_CODE and not prefix:
        language = ""
    i18n_url = urllib.parse.urljoin(language + "/", url)
    complete_url = urllib.parse.urljoin(get_host_url(request), i18n_url)
    return complete_url


def get_page(
    request,
    identifier="404",
    lang="",
    model_page=None,
    attr_page="identifier",
    model_content=None,
):
    if not model_content:
        model_content = apps.get_model(app_label="camomilla", model_name="Content")
    if not model_page:
        model_page = apps.get_model(app_label="camomilla", model_name="Page")
    if not lang:
        lang = get_language()
    kwargs = {attr_page: identifier}
    try:
        page = model_page.objects.prefetch_related("contents").get(**kwargs)
    except model_page.DoesNotExist:
        page, _ = model_page.objects.get_or_create(**kwargs)
    page = compile_seo(request, page, lang)
    return page


def get_seo_model(request, model, **params):
    seo_obj = find_or_redirect(request, model, **params)
    return compile_seo(request, seo_obj, get_language())


def compile_seo(request, seo_obj, lang=""):
    if not seo_obj.og_title:
        seo_obj.og_title = seo_obj.title
    if not seo_obj.og_description:
        seo_obj.og_description = seo_obj.description
    permalink = request.path
    if not seo_obj.permalink:
        seo_obj.permalink = permalink
    if not seo_obj.canonical:
        seo_obj.canonical = get_complete_url(request, permalink, lang)
    else:
        seo_obj.canonical = get_complete_url(request, seo_obj.canonical, lang)
    if not seo_obj.og_url:
        seo_obj.og_url = get_complete_url(request, permalink, lang)
    else:
        seo_obj.og_url = get_complete_url(request, seo_obj.og_url, lang)
    return seo_obj


def find_or_redirect(request, obj_class, **kwargs):
    try:
        obj = obj_class.objects.get(**kwargs)
        return obj
    except obj_class.DoesNotExist:
        cur_language = get_language()
        for language in settings.LANGUAGES:
            try:
                activate(language[0])
                obj = obj_class.objects.get(**kwargs)
                activate(cur_language)
                obj = obj_class.objects.get(pk=obj.pk)
                args = []
                for kwarg_key, kwarg_val in kwargs.items():
                    args.append(getattr(obj, kwarg_key))
                url_name = resolve(request.path_info).url_name
                language_path = reverse(url_name, args=args)
                raise NeedARedirect(language_path)
            except obj_class.DoesNotExist:
                pass
        activate(cur_language)
        raise Http404()
