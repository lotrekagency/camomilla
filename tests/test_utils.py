import os
import mock

from django.test import TestCase
from requests import RequestException

from django.test import RequestFactory


from camomilla.utils import get_article_with_seo, get_host_url, get_complete_url, get_seo
from camomilla.models import SitemapUrl, Article


class UtilsTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_host_url(self):
        """Our beloved get_host_url utility"""
        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        host_url = get_host_url(request)
        self.assertEqual(host_url, 'http://localhost')

    def test_get_complete_url(self):
        """Our beloved get_complete_url utility"""
        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        complete_url = get_complete_url(request, 'path')
        self.assertEqual(complete_url, 'http://localhost/path')
        complete_url = get_complete_url(request, 'path', 'it')
        self.assertEqual(complete_url, 'http://localhost/path')
        complete_url = get_complete_url(request, 'path', 'fr')
        self.assertEqual(complete_url, 'http://localhost/fr/path')

    def test_get_seo_clean(self):
        """Our beloved get_seo utility with auto attributes"""
        SitemapUrl.objects.language().create(page='path')

        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        seo_obj = get_seo(request, 'path')
        self.assertEqual(seo_obj.og_url, 'http://localhost/path')
        self.assertEqual(seo_obj.canonical, 'http://localhost/path')

        self.assertEqual(get_seo(request, 'notexist'), None)

    def test_get_seo_permalink(self):
        """Our beloved get_seo utility with auto attributes"""
        SitemapUrl.objects.language().create(
            page='path', permalink='perma/link'
        )

        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        seo_obj = get_seo(request, 'path')
        self.assertEqual(seo_obj.og_url, 'http://localhost/perma/link')
        self.assertEqual(seo_obj.canonical, 'http://localhost/perma/link')

    def test_get_seo_og_url(self):
        """Our beloved get_seo utility with auto attributes"""
        SitemapUrl.objects.language().create(
            page='path', canonical='canonical'
        )

        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        seo_obj = get_seo(request, 'path')
        self.assertEqual(seo_obj.og_url, 'http://localhost/canonical')
        self.assertEqual(seo_obj.canonical, 'http://localhost/canonical')

    def test_get_seo_combo_url(self):
        """Our beloved get_seo utility with auto attributes"""
        SitemapUrl.objects.language().create(
            page='path', permalink='perma/link',
            canonical='canonical', og_url='og_url'
        )

        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        seo_obj = get_seo(request, 'path')
        self.assertEqual(seo_obj.og_url, 'http://localhost/og_url')
        self.assertEqual(seo_obj.canonical, 'http://localhost/canonical')


    def test_get_article_with_seo(self):
        """Our beloved get_seo utility with auto attributes"""
        Article.objects.language().create(
            identifier='art1', permalink='perma/link',
            canonical='canonical', og_url='og_url'
        )

        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        article = get_article_with_seo(request, 'art1')
        self.assertEqual(article.og_url, 'http://localhost/og_url')
        self.assertEqual(article.canonical, 'http://localhost/canonical')
