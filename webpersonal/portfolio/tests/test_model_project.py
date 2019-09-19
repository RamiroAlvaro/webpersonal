from datetime import datetime
from django.test import TestCase
from webpersonal.portfolio.models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Un Título',
            description='Una Descripción',
            image='projects/cierre.jpg',
            link=''
        )

    def test_create(self):
        self.assertTrue(Project.objects.exists())

    def test_link_can_be_blank(self):
        field = Project._meta.get_field('link')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Un Título', str(self.project))

    def test_created(self):
        """Subscription must have an auto created at attr."""
        self.assertIsInstance(self.project.created, datetime)
