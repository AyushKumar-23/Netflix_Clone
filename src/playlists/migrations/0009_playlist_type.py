# Generated by Django 4.2 on 2023-04-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0008_tvshowproxy_tvshowseasonproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='type',
            field=models.CharField(choices=[('MOV', 'Movie'), ('TVS', 'TV Show'), ('SEA', 'Season'), ('PLY', 'Playlist')], default='PLY', max_length=3),
        ),
    ]