import os
import mock

from django.test import TestCase
from requests import RequestException

from django.test import RequestFactory


from camomilla.utils import get_host_url, get_complete_url, get_seo
from camomilla.models import SitemapUrl


class UtilsTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_host_url(self):
        """Our beloved get_host_url utility"""
        request_factory = RequestFactory()
        request = request_factory.get('/path', data={'name': 'test'})
        request.META['HTTP_HOST'] = 'localhost'
        host_url = get_host_url(request)
        self.assertEqual(host_url, 'http://localhost')

    def test_get_complete_url(self):
        """Our beloved get_complete_url utility"""
        request_factory = RequestFactory()
        request = request_factory.get('/path', data={'name': 'test'})
        request.META['HTTP_HOST'] = 'localhost'
        complete_url = get_complete_url(request, 'path')
        self.assertEqual(complete_url, 'http://localhost/path')
        complete_url = get_complete_url(request, 'path', 'it')
        self.assertEqual(complete_url, 'http://localhost/path')
        complete_url = get_complete_url(request, 'path', 'fr')
        self.assertEqual(complete_url, 'http://localhost/fr/path')

    def test_get_seo(self):
        """Our beloved get_seo utility"""
        SitemapUrl.objects.language().create(page='path')

        request_factory = RequestFactory()
        request = request_factory.get('/path', data={'name': 'test'})
        request.META['HTTP_HOST'] = 'localhost'
        seo_obj = get_seo(request, 'path')
        print (seo_obj)
