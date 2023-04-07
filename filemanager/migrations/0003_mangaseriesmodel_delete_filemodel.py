# Generated by Django 4.2 on 2023-04-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0002_rename_name_series_filemodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaSeriesModel',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
                ('author', models.TextField(null=True)),
                ('volume_total', models.IntegerField(null=True, verbose_name='Total Volumes')),
                ('chapter_total', models.IntegerField(null=True, verbose_name='Total Chapters')),
            ],
        ),
        migrations.DeleteModel(
            name='FileModel',
        ),
    ]
