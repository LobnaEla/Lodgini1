# Generated by Django 5.1.3 on 2024-11-21 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_userprofile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerprofile',
            name='country',
            field=models.CharField(max_length=15, null=True),
        ),
    ]