# Generated by Django 3.2.4 on 2021-06-26 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dimensions', '0005_auto_20210626_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyrate',
            old_name='Land_value',
            new_name='land_value',
        ),
    ]