# Generated by Django 4.0.3 on 2022-03-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_alter_climbsession_climber'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='blueprint',
            field=models.ImageField(null=True, upload_to='location/'),
        ),
    ]
