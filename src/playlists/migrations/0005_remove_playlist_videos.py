# Generated by Django 4.2 on 2023-04-09 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0004_alter_playlist_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='videos',
        ),
    ]
