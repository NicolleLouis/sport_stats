# Generated by Django 4.0.3 on 2022-03-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0013_alter_location_blueprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=24, null=True)),
            ],
        ),
    ]