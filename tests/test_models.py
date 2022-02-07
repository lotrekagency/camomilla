import os
import mock

from django.http import Http404
from django.test import TestCase
from django.test import RequestFactory
from django.utils.translation import activate, get_language

from camomilla.models import Article
from camomilla.templatetags.camomilla_filters import filter_content, alternate_urls

from requests import RequestException


class CamomillaFiltersTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_articles_with_auto_identifier(self):
        article1 = Article.objects.create(permalink="article-1")
        article2 = Article.objects.create(permalink="article-2")
        self.assertNotEqual(article1.identifier, article2.identifier)
