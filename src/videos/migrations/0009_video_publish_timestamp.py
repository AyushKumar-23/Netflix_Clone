# Generated by Django 4.2 on 2023-04-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
