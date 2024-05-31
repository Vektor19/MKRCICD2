from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __iter__(self):
        return iter(self.name)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
