# Generated by Django 4.1.2 on 2023-02-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_rename_emotion_gamestat_emotion_all_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestat',
            name='reviews_past_one_month',
            field=models.JSONField(default=dict),
        ),
    ]
