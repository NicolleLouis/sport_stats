# Generated by Django 4.0.3 on 2022-04-18 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0037_alter_climbuserstatcolor_number_of_routes_tried'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbsession',
            name='climber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='stats.climbuser'),
        ),
    ]
