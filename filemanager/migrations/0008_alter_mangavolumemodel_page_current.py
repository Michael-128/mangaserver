# Generated by Django 4.2 on 2023-04-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0007_alter_mangavolumemodel_page_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangavolumemodel',
            name='page_current',
            field=models.IntegerField(default=1),
        ),
    ]