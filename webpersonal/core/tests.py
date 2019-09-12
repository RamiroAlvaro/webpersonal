from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use core/home.html"""
        self.assertTemplateUsed(self.response, 'core/home.html')

    def test_html(self):
        contents = ('Ramiro Alvaro',
                    'Análise e Desenvolvimento de Sistemas',
                    )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class AboutTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('about'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use core/about.html"""
        self.assertTemplateUsed(self.response, 'core/about.html')

    def test_html(self):
        contents = ('Acerca de',
                    'Biografía',
                    'Ramiro Alvaro'
                    )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


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
