from django.test import TestCase
from .models import Modules

# Create your tests here.

class TestModulesManager(TestCase):

    def test_create_module(self):
        new_module = Modules.objects.create(
            nom='Module Test',
            code='module_test',
            description='Module de test',
            prix=0,
            isEnabled=True
        )

        self.assertEqual(new_module.nom, 'Module Test')