# Generated by Django 3.2.4 on 2021-06-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titleOwner', '0003_titleownerrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titleownerrelation',
            name='owners',
            field=models.CharField(max_length=191, null=True),
        ),
        migrations.AlterField(
            model_name='titleownerrelation',
            name='title_no',
            field=models.CharField(max_length=191),
        ),
    ]
