# Generated by Django 4.1.3 on 2022-11-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
    ]