# Generated by Django 5.1.3 on 2024-11-30 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_property_owner'),
        ('profile', '0014_rename_username_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='profile.ownerprofile'),
        ),
    ]