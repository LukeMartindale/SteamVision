# Generated by Django 4.1.2 on 2023-01-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_review_author_id_alter_review_review_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sentimenr_pos',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='review',
            name='sentiment_polarity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='sentiment_subjectivity',
            field=models.FloatField(default=0),
        ),
    ]
