# Generated by Django 4.1.13 on 2023-11-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_friends_delete_friendship'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
