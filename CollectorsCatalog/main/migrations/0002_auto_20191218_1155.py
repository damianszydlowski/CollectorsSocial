# Generated by Django 2.2.6 on 2019-12-18 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birthDate',
            new_name='birth_date',
        ),
    ]
