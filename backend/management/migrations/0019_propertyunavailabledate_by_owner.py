<<<<<<< HEAD
# Generated by Django 5.1.4 on 2024-12-24 12:04
=======
# Generated by Django 5.1.3 on 2024-12-28 11:52
>>>>>>> loblob

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_review_about_lodgini_alter_review_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyunavailabledate',
            name='by_owner',
            field=models.BooleanField(default=False),
        ),
    ]
