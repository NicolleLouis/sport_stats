# Generated by Django 4.0.3 on 2022-03-09 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_sport_sportsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbsession',
            name='climber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stats.climbuser'),
        ),
    ]