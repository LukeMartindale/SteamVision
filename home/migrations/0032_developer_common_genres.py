# Generated by Django 4.1.2 on 2023-03-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_developer_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='common_genres',
            field=models.JSONField(default=dict),
        ),
    ]