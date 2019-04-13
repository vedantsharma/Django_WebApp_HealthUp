from django.test import TestCase, Client
from django.urls import reverse, resolve
from HealthUp_Dj.core.views import home, signup, upload, pres_list, delete_pres
from HealthUp_Dj.core.models import Prescription
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_home = reverse('home')
        self.test_signup = reverse('signup')
        self.test_upload = reverse('upload')
        self.test_pres_list = reverse('pres_list')

    def test_home(self):
        response = self.client.get(self.test_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_signup_Get(self):
        response = self.client.get(self.test_signup)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_upload(self):
        Prescription.objects.create(
            title='hello',
            patient='aztek'
        )

        response = self.client.get(self.test_upload)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')

    def test_pres_list(self):
        response = self.client.get(self.test_pres_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescription_list.html')
