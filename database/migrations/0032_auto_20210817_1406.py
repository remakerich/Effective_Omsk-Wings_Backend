# Generated by Django 3.2.6 on 2021-08-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0031_season_trophy'),
    ]

    operations = [
        migrations.AddField(
            model_name='trophy',
            name='team',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trophy',
            name='place',
            field=models.IntegerField(choices=[(1, '1 место'), (2, '2 место'), (3, '3 место')]),
        ),
    ]
