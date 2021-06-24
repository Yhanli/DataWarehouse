# Generated by Django 3.2.4 on 2021-06-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TitleOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WKT', models.TextField(null=True)),
                ('title_no', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100, null=True)),
                ('land_district', models.CharField(max_length=100, null=True)),
                ('issue_date', models.DateTimeField(null=True)),
                ('guarantee_status', models.CharField(max_length=100, null=True)),
                ('estate_description', models.TextField(max_length=1000, null=True)),
                ('owners', models.CharField(max_length=1000, null=True)),
                ('spatial_extents_shared', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
