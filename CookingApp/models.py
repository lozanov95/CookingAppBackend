from django.db import models
from django.contrib.auth.models import User


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
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.difficulty}'


class Comment(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author_id}, created on {self.created_time}'
