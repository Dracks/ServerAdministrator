from django.test import TestCase

# Create your tests here.
from deployment import models


class VersionGetNextVersionTest(TestCase):

    def setUp(self):
        self.app=models.Application(name="Test1")
        self.app.save()

    def test_no_versions(self):
        self.assertEqual(models.Version.get_next_version(self.app), 1)

    def test_one_version(self):
        previous=models.Version(application=self.app, version=2)
        previous.save()
        self.assertEqual(models.Version.get_next_version(self.app), 3)