# Generated by Django 3.2.9 on 2021-12-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_wav', '0008_auto_20210914_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersong',
            name='give_image',
            field=models.ImageField(upload_to='give_image/'),
        ),
    ]