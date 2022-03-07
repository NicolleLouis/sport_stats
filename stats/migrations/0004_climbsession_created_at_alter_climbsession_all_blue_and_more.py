# Generated by Django 4.0.3 on 2022-03-06 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_climbsession_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbsession',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='climbsession',
            name='all_blue',
            field=models.IntegerField(default=0, verbose_name='Toutes les bleues'),
        ),
        migrations.AlterField(
            model_name='climbsession',
            name='all_red',
            field=models.IntegerField(default=0, verbose_name='Toutes les rouges'),
        ),
        migrations.AlterField(
            model_name='climbsession',
            name='duration',
            field=models.IntegerField(default=60, verbose_name='Durée (en min)'),
        ),
        migrations.AlterField(
            model_name='climbsession',
            name='new_blue',
            field=models.IntegerField(default=0, verbose_name='Nombre de nouvelles bleues'),
        ),
        migrations.AlterField(
            model_name='climbsession',
            name='new_red',
            field=models.IntegerField(default=0, verbose_name='Nombre de nouvelles rouges'),
        ),
    ]