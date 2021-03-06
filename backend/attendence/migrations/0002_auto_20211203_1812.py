# Generated by Django 3.2.9 on 2021-12-03 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='student',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendence',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='attendence',
            unique_together={('section', 'date', 'course_code')},
        ),
    ]
