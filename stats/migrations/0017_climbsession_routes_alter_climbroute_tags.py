# Generated by Django 4.0.3 on 2022-03-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0016_climbroute'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbsession',
            name='routes',
            field=models.ManyToManyField(blank=True, null=True, to='stats.climbroute'),
        ),
        migrations.AlterField(
            model_name='climbroute',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='routes', to='stats.routetag'),
        ),
    ]