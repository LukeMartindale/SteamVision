# Generated by Django 4.1.2 on 2023-01-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_review_review_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='review',
            name='review_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
