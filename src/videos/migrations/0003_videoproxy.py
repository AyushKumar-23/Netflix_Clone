# Generated by Django 4.2 on 2023-04-06 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_video_description_alter_video_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
