# Generated by Django 3.2.6 on 2021-08-06 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_alter_partner_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StaffMember',
            new_name='Employee',
        ),
    ]
