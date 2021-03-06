# Generated by Django 4.0.3 on 2022-04-14 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0032_climbuserstatcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbuserstatcolor',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='climbuserstatcolor',
            name='climb_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_stats', to='stats.climbuser'),
        ),
    ]
