from django.test import TestCase
from .models import Category,Recipe

# Create your tests here.
class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Appetizer')
        
    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_iter_method(self):
        category = Category.objects.get(id=1)
        self.assertEquals(list(iter(category)), list(iter('Appetizer')))


    def test_str_method(self):
        category = Category.objects.get(id=1)
        self.assertEquals(str(category), 'Appetizer')