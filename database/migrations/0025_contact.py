# Generated by Django 3.2.6 on 2021-08-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0024_auto_20210815_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('line1', models.CharField(max_length=100, verbose_name='Fist Line')),
                ('line2', models.CharField(default=None, max_length=100, verbose_name='Second Line')),
                ('line3', models.CharField(default=None, max_length=100, verbose_name='Third Line')),
            ],
        ),
    ]