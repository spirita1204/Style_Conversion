# Generated by Django 3.1.3 on 2021-01-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_wav', '0005_remove_usersong_audio_file_output'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersong',
            name='title',
        ),
    ]