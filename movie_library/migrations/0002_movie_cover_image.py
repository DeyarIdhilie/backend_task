# Generated by Django 4.1 on 2022-08-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
