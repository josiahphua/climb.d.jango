# Generated by Django 3.2.5 on 2021-07-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_route_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='climb_type',
            field=models.CharField(choices=[('BD', 'Boulder'), ('TR', 'Toprope'), ('LD', 'Lead'), ('SP', 'Speed')], default='BD', max_length=2),
        ),
    ]
