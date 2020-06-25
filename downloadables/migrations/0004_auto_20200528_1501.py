# Generated by Django 3.0.3 on 2020-05-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloadables', '0003_auto_20200528_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadablefile',
            name='is_accessible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='downloadablefile',
            name='is_ece',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='downloadablefile',
            name='is_ee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='downloadablefile',
            name='is_tutorial',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='downloadable',
            name='files',
            field=models.ManyToManyField(blank=True, to='downloadables.DownloadableFile'),
        ),
        migrations.AlterField(
            model_name='downloadable',
            name='is_accessible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='downloadable',
            name='is_ece',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='downloadable',
            name='is_ee',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='downloadable',
            name='is_tutorial',
            field=models.BooleanField(default=False),
        ),
    ]
