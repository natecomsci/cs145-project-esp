# Generated by Django 5.2 on 2025-05-12 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_stoplight_direction_stoplight_lookahead_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stoplight',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='stoplight',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='stoplight',
            name='local_id',
        ),
    ]
