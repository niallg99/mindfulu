# Generated by Django 4.1.13 on 2023-12-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_profileinfo_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='streak_count',
            field=models.IntegerField(default=0),
        ),
    ]
