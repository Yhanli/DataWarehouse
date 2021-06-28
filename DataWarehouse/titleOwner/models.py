from django.db import models


# Create your models here.

class TitleOwner(models.Model):
    WKT = models.TextField(null=True)
    title_no = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    land_district = models.CharField(max_length=100, null=True)
    issue_date = models.DateTimeField(null=True)
    guarantee_status = models.CharField(max_length=100, null=True)
    estate_description = models.TextField(max_length=1000, null=True)
    owners = models.CharField(max_length=10000, null=True)
    spatial_extents_shared = models.CharField(max_length=100, null=True)


class TitleOwnerRelation(models.Model):
    title_no = models.CharField(max_length=191)
    land_district = models.CharField(max_length=100, null=True)
    issue_date = models.DateTimeField(null=True)
    owners = models.CharField(max_length=191, null=True)
