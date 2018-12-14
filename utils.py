from django.conf import settings
import urllib.parse
from django.utils.translation import get_language

from django.apps import apps
from django.http import QueryDict
import json
from rest_framework import parsers
from functools import reduce
from django.http.multipartparser import MultiPartParser as DjangoMultiPartParser
from django.http.multipartparser import MultiPartParserError
from rest_framework.exceptions import ParseError
from django.utils import six


class MultipartJsonParser(parsers.BaseParser):

    media_type = 'multipart/form-data'

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        request = parser_context['request']
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        meta = request.META.copy()
        meta['CONTENT_TYPE'] = media_type
        upload_handlers = request.upload_handlers

        try:
            parser = DjangoMultiPartParser(meta, stream, upload_handlers, encoding)
            data, files = parser.parse()
            result = parsers.DataAndFiles(data, files)
            data = {}
            data = json.loads(result.data["data"])
            for key, value in result.files.items():
                reduce(lambda d, k: d.setdefault(k, {}),key.split('.')[:-1],data).update({key.split('.')[-1]: value})
            return data
        except MultiPartParserError as exc:
            raise ParseError('Multipart form parse error - %s' % six.text_type(exc))


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


def get_page(request, identifier='404', lang='', model=None, attr='page'):
    if not model:
        model = apps.get_model(app_label='camomilla', model_name='SitemapUrl')
    if not lang:
        lang = get_language()
    try:
        kwargs = {attr: identifier}
        meta_tag, _ = model.objects.language().fallbacks().get_or_create(**kwargs)
        return compile_seo(request, meta_tag, lang)
    except model.DoesNotExist:
        return None


def compile_seo(request, seo_obj, lang=''):
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
        seo_obj.og_url = get_complete_url(request, seo_obj.og_url,lang)
    return seo_obj


def get_seo(request, identifier='', lang='', model=None, attr='identifier', seo_obj=None):
    if seo_obj: return compile_seo(request, seo_obj, lang)
    elif not identifier: 
        raise TypeError("get_seo() missing 1 required positional argument: 'identifier'\n"+
        "identifier is required when no seo_obj is provided")
    else: return get_page(request, identifier, lang, model, attr)


def get_article_with_seo(request, identifier, lang=''):
    return get_seo(
        request, identifier, 
        lang, apps.get_model(app_label='camomilla', model_name='Article'), 
        'identifier'
    )
