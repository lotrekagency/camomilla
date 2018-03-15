from django.conf import settings
import urllib.parse
from django.utils.translation import get_language

from django.apps import apps


def get_host_url(request):
    if request:
        return '{0}://{1}'.format(
            request.scheme, request.META['HTTP_HOST']
        )


def get_complete_url(request, url, language=''):
    prefix = getattr(settings, 'PREFIX_DEFAULT_LANGUAGE', False)
    if language == settings.LANGUAGE_CODE and not prefix:
        language = ''
    i18n_url = urllib.parse.urljoin(language + '/', url)
    complete_url = urllib.parse.urljoin(get_host_url(request), i18n_url)
    return complete_url


def get_page(request, identifier, lang='', model=None, attr='page'):
    if not model:
        model = apps.get_model(app_label='camomilla', model_name='SitemapUrl')
    if not lang:
        lang = get_language()
    try:
        kwargs = {attr: identifier}
        meta_tag = model.objects.language().get(**kwargs)
        if not meta_tag.og_title:
            meta_tag.og_title = meta_tag.title
        if not meta_tag.og_description:
            meta_tag.og_description = meta_tag.description
        permalink = request.path
        if not meta_tag.permalink:
            meta_tag.permalink = permalink
        if not meta_tag.canonical:
            meta_tag.canonical = get_complete_url(request, permalink, lang)
        else:
            meta_tag.canonical = get_complete_url(request, meta_tag.canonical, lang)
        if not meta_tag.og_url:
            meta_tag.og_url = meta_tag.canonical
        else:
            meta_tag.og_url = get_complete_url(request, meta_tag.og_url,lang)
        return meta_tag

    except model.DoesNotExist:
        return None


def get_seo(request, identifier, lang='', model=None, attr='identifier'):
    if not model:
        model = apps.get_model(app_label='camomilla', model_name='SitemapUrl')
    return get_page(request, identifier, lang, model, attr)


def get_article_with_seo(request, identifier, lang=''):
    return get_seo(
        request, identifier, 
        lang, apps.get_model(app_label='camomilla', model_name='Article'), 
        'identifier'
    )
