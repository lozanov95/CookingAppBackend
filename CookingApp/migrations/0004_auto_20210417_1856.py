# Generated by Django 3.2 on 2021-04-17 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CookingApp', '0003_recipe_creator_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='PreparationSteps',
        ),
    ]
