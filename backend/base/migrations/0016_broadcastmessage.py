# Generated by Django 4.1.13 on 2023-12-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_friends_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]