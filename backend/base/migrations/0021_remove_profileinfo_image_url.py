# Generated by Django 4.1.13 on 2023-12-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_profileinfo_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileinfo',
            name='image_url',
        ),
    ]
