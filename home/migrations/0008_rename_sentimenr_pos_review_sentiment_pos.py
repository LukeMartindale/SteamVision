# Generated by Django 4.1.2 on 2023-01-18 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_review_sentimenr_pos_review_sentiment_polarity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='sentimenr_pos',
            new_name='sentiment_pos',
        ),
    ]
