# Generated by Django 3.2.5 on 2021-07-03 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_alter_userprofile_last_request_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_request_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 20, 42, 15, 376319)),
        ),
    ]