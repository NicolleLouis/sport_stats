# Generated by Django 4.0.3 on 2022-03-16 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0023_alter_climbroute_color'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='climbroutetry',
            unique_together={('climb_session', 'climb_route')},
        ),
    ]
