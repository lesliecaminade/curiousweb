# Generated by Django 3.0.3 on 2020-06-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200604_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='type',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]
