# Generated by Django 4.0.3 on 2022-03-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClimbSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('new_blue', models.IntegerField(default=0)),
                ('all_blue', models.IntegerField(default=0)),
                ('new_red', models.IntegerField(default=0)),
                ('all_red', models.IntegerField(default=0)),
                ('climber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stats.user')),
            ],
        ),
    ]