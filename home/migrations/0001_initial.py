# Generated by Django 4.1.2 on 2023-01-17 15:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('app_id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='game', max_length=100)),
                ('description', models.TextField(default='description')),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('developer', models.JSONField(default=dict)),
                ('publisher', models.JSONField(default=dict)),
                ('categories', models.JSONField(default=dict)),
                ('supported_languages', models.TextField(default='Languages')),
                ('header_image', models.URLField(default='https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('author', models.JSONField(default=dict)),
                ('language', models.CharField(default='english', max_length=50)),
                ('review_text', models.TextField(default='')),
                ('time_created', models.DateField(default=django.utils.timezone.now)),
                ('time_updated', models.DateField(default=django.utils.timezone.now)),
                ('voted_up', models.BooleanField(default=False)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_funny', models.IntegerField(default=0)),
                ('purchase_on_steam', models.BooleanField(default=True)),
                ('received_for_free', models.BooleanField(default=False)),
                ('written_during_early_access', models.BooleanField(default=False)),
                ('app', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.game')),
            ],
        ),
    ]
