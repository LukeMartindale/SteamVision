# Generated by Django 4.1.2 on 2023-01-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_sentimenr_pos_review_sentiment_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='emotion_prominent',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='review',
            name='emotion_scores',
            field=models.JSONField(default=dict),
        ),
    ]
