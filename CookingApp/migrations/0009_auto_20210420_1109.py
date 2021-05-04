# Generated by Django 3.2 on 2021-04-20 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CookingApp', '0008_alter_comment_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='creator_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]