# Generated by Django 4.1.2 on 2023-02-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_gamestat_sentiment_all_time_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestat',
            name='sentiment_past_one_month',
            field=models.JSONField(default=dict),
        ),
    ]
