# Generated by Django 3.2.6 on 2021-08-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0033_remove_trophy_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=300)),
            ],
        ),
    ]
