# Generated by Django 4.1.2 on 2023-02-27 22:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_gamestat_emotion_all_time_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestat',
            name='current_review_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='highest_review_score_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]