# Generated by Django 3.2 on 2021-04-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(max_length=4096),
        ),
    ]