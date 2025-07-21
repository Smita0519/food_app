from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)