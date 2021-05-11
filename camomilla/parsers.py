import json
import six

from django.http.multipartparser import MultiPartParser as DjangoMultiPartParser
from django.http.multipartparser import MultiPartParserError
from django.conf import settings
from functools import reduce
from rest_framework import parsers
from rest_framework.exceptions import ParseError
from django.conf import settings

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

