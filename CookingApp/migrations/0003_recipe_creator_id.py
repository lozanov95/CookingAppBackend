# Generated by Django 3.2 on 2021-04-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookingApp', '0002_alter_recipe_preparation_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='creator_id',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
