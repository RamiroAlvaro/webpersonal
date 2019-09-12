from django.test import TestCase
from django.shortcuts import resolve_url as r


class ContactTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('contact'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use core/about.html"""
        self.assertTemplateUsed(self.response, 'core/contact.html')

    def test_html(self):
        contents = ('Contacto',
                    'Asesoría',
                    'Teléfono:',
                    '31-99138-7178'
                    )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
