# Generated by Django 3.2.6 on 2021-08-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=10)),
                ('number', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
