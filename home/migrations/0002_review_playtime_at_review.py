# Generated by Django 4.1.2 on 2023-01-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='playtime_at_review',
            field=models.IntegerField(default=0),
        ),
    ]
