# Generated by Django 4.0.3 on 2022-04-14 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0033_climbuserstatcolor_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='climbuser',
            name='number_of_blues',
        ),
        migrations.RemoveField(
            model_name='climbuser',
            name='number_of_red',
        ),
    ]