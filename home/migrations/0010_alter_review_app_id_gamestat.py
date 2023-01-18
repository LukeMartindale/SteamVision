# Generated by Django 4.1.2 on 2023-01-18 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_review_emotion_prominent_review_emotion_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='app_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game'),
        ),
        migrations.CreateModel(
            name='GameStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.JSONField(default=dict)),
                ('emotion', models.JSONField(default=dict)),
                ('app_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.game')),
            ],
        ),
    ]