from django.test import TestCase
from .models import Category,Recipe

# Create your tests here.
class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Appetizer')
