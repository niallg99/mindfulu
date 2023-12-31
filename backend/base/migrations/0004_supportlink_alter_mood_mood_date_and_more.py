# Generated by Django 4.1.13 on 2023-11-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('link_text', models.CharField(max_length=200)),
                ('link_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Support Link',
                'verbose_name_plural': 'Support Links',
            },
        ),
        migrations.AlterField(
            model_name='mood',
            name='mood_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='moodcause',
            name='cause_type',
            field=models.CharField(choices=[('Academic', 'Academic'), ('Financial', 'Financial'), ('Relationship/Social', 'Relationship/Social'), ('Other', 'Other')], max_length=50),
        ),
    ]
