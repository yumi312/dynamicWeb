# Generated by Django 4.0.3 on 2022-06-14 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_log_latest_edit_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='latest_edit_time',
            new_name='edit_time',
        ),
    ]
