# Generated by Django 5.1.3 on 2024-11-24 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0011_userprofile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownerprofile',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='username',
        ),
    ]