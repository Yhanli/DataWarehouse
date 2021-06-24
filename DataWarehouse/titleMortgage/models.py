from django.db import models


# Create your models here.
class TitleMortgage(models.Model):
    title_no = models.CharField(max_length=100)
    land_district = models.CharField(max_length=100)
    memorial_text = models.TextField(null=True)
    current = models.CharField(max_length=100, null=True)
    instrument_number = models.CharField(max_length=100, null=True)
    instrument_lodged_datetime = models.DateTimeField(null=True)
    instrument_type = models.CharField(max_length=100, null=True)
    encumbrancees = models.CharField(max_length=1000,null=True)
