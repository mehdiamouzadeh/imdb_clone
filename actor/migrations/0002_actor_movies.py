# Generated by Django 3.1.2 on 2020-11-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='movie.Movie'),
        ),
    ]
