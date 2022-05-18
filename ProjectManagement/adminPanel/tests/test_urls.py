from django.test import SimpleTestCase
from django.urls import reverse, resolve
from adminPanel.views import searchAsso,showActivityTracking

class TestUrls(SimpleTestCase):
    def test_searchAsso_url_is_resolved(self):
        url = reverse('searchAsso')
        self.assertEqual(resolve(url).func, searchAsso)

    def test_searchAsso_url_is_resolved(self):
        url = reverse('showActivityTracking')
        self.assertEqual(resolve(url).func, showActivityTracking)   

        