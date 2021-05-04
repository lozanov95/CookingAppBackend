from rest_framework import serializers
from .models import Recipe, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    users = User.objects.all()
    author_id = serializers.SlugRelatedField(queryset=users, slug_field='username')

    class Meta:
        model = Comment
        fields = ['id', 'author_id', 'recipe', 'content', 'created_time']


class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredients', 'preparation_steps', 'difficulty', 'image_url', 'created_time',
                  'creator_id', 'comments']
