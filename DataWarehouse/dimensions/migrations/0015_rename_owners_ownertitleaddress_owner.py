# Generated by Django 3.2.4 on 2021-06-28 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dimensions', '0014_ownertitleaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownertitleaddress',
            old_name='owners',
            new_name='owner',
        ),
    ]
