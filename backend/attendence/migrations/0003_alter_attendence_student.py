# Generated by Django 3.2.9 on 2021-12-03 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendence', '0002_auto_20211203_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='student',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
