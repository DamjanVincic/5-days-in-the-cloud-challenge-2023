# Generated by Django 4.2.6 on 2023-11-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_advancedstatistics_shotstatistics_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gamesPlayed',
            field=models.IntegerField(default=1),
        ),
    ]
