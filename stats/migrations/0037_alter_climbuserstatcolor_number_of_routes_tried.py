# Generated by Django 4.0.3 on 2022-04-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0036_climbsessionstatcolor_routes_flashed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbuserstatcolor',
            name='number_of_routes_tried',
            field=models.IntegerField(default=0, verbose_name='Nombre total de pistes essayées'),
        ),
    ]
