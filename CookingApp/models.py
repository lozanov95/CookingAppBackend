from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    amount = models.IntegerField()
    measurement_unit = models.CharField(max_length=10)


class PreparationSteps(models.Model):
    name = models.CharField(max_length=120)
    needed_time = models.CharField(max_length=10)


class Recipe(models.Model):
    DIFFICULTIES = (
        ('Easy', 'EASY'),
        ('Medium', 'MEDIUM'),
        ('Hard', 'HARD')
    )
    name = models.CharField(max_length=128)
    ingredients = models.TextField(max_length=1024)
    preparation_steps = models.TextField(max_length=4096)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTIES)
    image_url = models.URLField()
    created_time = models.DateTimeField(auto_now=True)
    creator_id = models.CharField(max_length=10)
