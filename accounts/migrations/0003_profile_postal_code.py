# Generated by Django 5.0.7 on 2024-07-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
