# Generated by Django 4.1.13 on 2023-11-01 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_event_scrapeddata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]