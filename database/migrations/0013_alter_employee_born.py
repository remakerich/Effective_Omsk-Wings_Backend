# Generated by Django 3.2.6 on 2021-08-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20210806_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='born',
            field=models.DateField(null=True),
        ),
    ]
