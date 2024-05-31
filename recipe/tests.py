from django.test import TestCase
from .models import Category,Recipe
from django.utils import timezone

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

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Main Dish')
        Recipe.objects.create(
            title='Spaghetti Bolognese',
            description='A classic Italian pasta dish with meat sauce',
            instructions='1. Cook the pasta. 2. Prepare the meat sauce. 3. Mix and serve.',
            ingredients='Pasta, Ground beef, Tomato sauce, Onion, Garlic',
            created_at=timezone.now(),
            updated_at=timezone.now(),
            category=category
        )

    def test_title_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_str_method(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEquals(str(recipe), 'Spaghetti Bolognese')

    def test_recipe_category(self):
        recipe = Recipe.objects.get(id=1)
        category = recipe.category
        self.assertEquals(category.name, 'Main Dish')
