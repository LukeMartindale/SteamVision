# Generated by Django 4.1.2 on 2023-03-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_gamestat_highest_review_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='games',
            field=models.JSONField(default=dict),
        ),
    ]
