# Generated by Django 3.2.6 on 2021-08-17 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0029_auto_20210817_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediaalbum',
            name='album_description',
        ),
        migrations.RemoveField(
            model_name='mediafile',
            name='mediafile_description',
        ),
    ]
