# Generated by Django 3.2.5 on 2021-07-12 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_routes_tracker_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='route_id',
            new_name='id',
        ),
    ]