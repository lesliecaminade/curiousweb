# Generated by Django 3.0.3 on 2020-05-15 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentstutorial_app', '0002_auto_20200515_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttutorial',
            name='scholarships',
        ),
    ]
