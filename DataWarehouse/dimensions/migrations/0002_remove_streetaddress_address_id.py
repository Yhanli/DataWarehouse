# Generated by Django 3.2.4 on 2021-06-24 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dimensions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streetaddress',
            name='address_id',
        ),
    ]
