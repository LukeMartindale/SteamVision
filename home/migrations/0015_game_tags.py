# Generated by Django 4.1.2 on 2023-02-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_descriptor'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.JSONField(default=dict),
        ),
    ]
