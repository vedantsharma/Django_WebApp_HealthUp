from django.test import SimpleTestCase
from django.urls import reverse, resolve
from HealthUp_Dj.core.views import home, signup, upload, pres_list, delete_pres

class TestUrls(SimpleTestCase):

    def test_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_home_url(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_upload_url(self):
        url = reverse('upload')
        self.assertEqual(resolve(url).func, upload)

    def test_prescription_url(self):
        url = reverse('pres_list')
        self.assertEqual(resolve(url).func, pres_list)

    def test_delete_url(self):
        url = reverse('delete_pres', kwargs={'pk' : 1})
        self.assertEqual(resolve(url).func, delete_pres)