# Generated by Django 4.2 on 2023-04-06 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='name_series',
            new_name='name',
        ),
    ]