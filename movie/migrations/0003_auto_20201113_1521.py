# Generated by Django 3.1.2 on 2020-11-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20201105_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Poster',
            field=models.ImageField(blank=True, upload_to='movies'),
        ),
    ]