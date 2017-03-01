from .models import SitemapUrl
import urllib.parse


def get_complete_url(request, url, language=''):
    if language == settings.LANGUAGE_CODE:
        if settings.PREFIX_DEFAULT_LANGUAGE:
            language = ''
    i18n_url = urllib.parse.urljoin(language + '/', url)
    complete_url = urllib.parse.urljoin(settings.SITE_URL, i18n_url)
    return complete_url


def get_seo(request, page_requested):
    try:
        meta_tag = SitemapUrl.objects.language().get(page=page_requested)
        if not meta_tag.og_title:
            meta_tag.og_title = meta_tag.title
        if not meta_tag.og_description:
            meta_tag.og_description = meta_tag.description
        meta_tag.canonical = get_complete_url(request, meta_tag.canonical)
        if not meta_tag.og_url:
            meta_tag.og_url = meta_tag.canonical
        else:
            meta_tag.og_url = get_complete_url(request, meta_tag.og_url)
        return meta_tag
    except SitemapUrl.DoesNotExist:
        return None
