# Generated by Django 5.2.3 on 2025-06-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
