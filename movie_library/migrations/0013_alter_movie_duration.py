# Generated by Django 4.1 on 2022-08-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_library', '0012_alter_movie_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
