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



        data = {}
        data = json.loads(result.data["data"])
        for key, value in result.files.items():
            reduce(lambda d, k: d.setdefault(k, {}),key.split('.')[:-1],data).update({key.split('.')[-1]: value})
        return parsers.DataAndFiles(data, result.files)
        # return data

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
        meta_tag, _ = model.objects.language().fallbacks().get_or_create(**kwargs)
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
