from django.conf import settings
import urllib.parse
from django.utils.translation import get_language
from .models import SitemapUrl


def get_complete_url(request, url, language=''):
    if language == settings.LANGUAGE_CODE:
        if settings.PREFIX_DEFAULT_LANGUAGE:
            language = ''
    i18n_url = urllib.parse.urljoin(language + '/', url)
    complete_url = urllib.parse.urljoin(settings.SITE_URL, i18n_url)
    return complete_url



def get_seo(request, page_requested, lang='', model=SitemapUrl):
    if not lang:
        lang = get_language()
    try:
        meta_tag = model.objects.language().get(page=page_requested)
        if not meta_tag.og_title:
            meta_tag.og_title = meta_tag.title
        if not meta_tag.og_description:
            meta_tag.og_description = meta_tag.description
        if not meta_tag.canonical:
            meta_tag.canonical = get_complete_url(request, meta_tag.permalink,lang)
        else:
            meta_tag.canonical = get_complete_url(request, meta_tag.canonical,lang)
        if not meta_tag.og_url:
            meta_tag.og_url = meta_tag.canonical
        else:
            meta_tag.og_url = get_complete_url(request, meta_tag.og_url,lang)
        return meta_tag
    except model.DoesNotExist:
        return None
