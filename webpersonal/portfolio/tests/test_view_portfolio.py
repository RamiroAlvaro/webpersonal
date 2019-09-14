from django.test import TestCase
from django.shortcuts import resolve_url as r
from webpersonal.portfolio.models import Project


class PortfolioTest(TestCase):
    def setUp(self):
        Project.objects.create(
            title='Título del proyecto',
            description='Descripción del proyecto',
            image='projects/cierre.jpg',
            link=''
        )
        self.response = self.client.get(r('portfolio'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use portfolio/portfolio.html"""
        self.assertTemplateUsed(self.response, 'portfolio/portfolio.html')

    def test_html(self):
        contents = ('Portafolio',
                    'Currículo',
                    'Título del proyecto',
                    'Descripción del proyecto',
                    'projects/cierre.jpg',
                    )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        key = 'projects'
        self.assertIn(key, self.response.context)


