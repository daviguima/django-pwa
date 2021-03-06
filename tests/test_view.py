from django.test import TestCase
from django.shortcuts import resolve_url as r


class ServiceWorkerTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('serviceworker'))

    def test_get(self):
        """GET /serviceworker.js Should return status code 200"""
        self.assertEqual(200, self.response.status_code)


class ManifestTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('manifest'), format='json')

    def test_get(self):
        """GET /manifest.json Should return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must have the template manifest.json"""
        self.assertTemplateUsed(self.response, 'manifest.json')

    def test_manifest_contains(self):
        """Must be the attributes to manitesf.json"""
        contents = [
            '"name":',
            '"short_name":',
            '"description":',
            '"start_url":',
            '"display":',
            '"background_color":',
            '"theme_color":',
            '"orientation":',
            '"icons":',
            '"dir":',
            '"lang":'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
