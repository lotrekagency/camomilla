import os
import mock

from django.http import Http404
from django.test import TestCase
from django.test import RequestFactory
from django.utils.translation import activate, get_language

from camomilla.models import Page, Article
from camomilla.templatetags.camomilla_filters import filter_content, alternate_urls

from requests import RequestException


class CamomillaFiltersTestCase(TestCase):
    def setUp(self):
        pass

    def test_filter_content(self):
        request_factory = RequestFactory()
        request = request_factory.get("/path")
        request.META["HTTP_HOST"] = "localhost"
        page = Page.get(request, identifier="home")
        content = filter_content(page, "content1")
        self.assertEqual(content.identifier, "content1")
        self.assertEqual(content.content, "")
        content.content = "Hello World!"
        content.save()
        page = Page.get(request, identifier="home")
        content = filter_content(page, "content1")
        self.assertEqual(content.identifier, "content1")
        self.assertEqual(content.content, "Hello World!")

    def test_filter_alternate_urls(self):
        request = RequestFactory().get("/path", HTTP_HOST="localhost:8000")
        request.META["HTTP_HOST"] = "localhost"
        page = Page.get(request, identifier="home")
        alt_urls = dict(alternate_urls(page, request))
        self.assertEqual(alt_urls, {})

        request = RequestFactory().get("/about", HTTP_HOST="localhost:8000")
        request.META["HTTP_HOST"] = "localhost"
        page = Page.get(request, identifier="about")
        alt_urls = dict(alternate_urls(page, request))
        self.assertEqual(alt_urls["it"], "http://localhost/about")
        self.assertEqual(alt_urls["en"], "http://localhost/en/about")
        self.assertEqual(alt_urls["de"], "http://localhost/de/about")
