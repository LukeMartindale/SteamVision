# Generated by Django 4.1.2 on 2022-12-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_reviewdata_reviewsstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsstat',
            name='sentiment',
            field=models.JSONField(default={'label': '-1', 'value': 2}),
        ),
    ]