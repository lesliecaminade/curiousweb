# Generated by Django 3.0.3 on 2020-06-04 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app_2', '0004_auto_20200531_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
