# Generated by Django 3.2.6 on 2021-08-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_staffmember_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmember',
            name='department',
            field=models.CharField(choices=[('Руководство', 'Руководство'), ('Тренерский штаб', 'Тренерский штаб'), ('Персонал', 'Персонал')], max_length=20),
        ),
    ]
