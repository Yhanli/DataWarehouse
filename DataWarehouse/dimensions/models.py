from django.db import models


# Create your models here.

class AimAddress(models.Model):
    # address_id = id
    change_id = models.IntegerField(null=True, db_index=True)
    primary_address_id = models.IntegerField(null=True, db_index=True)
    address_lifecycle_stage = models.CharField(max_length=100, null=True)
    address_provider = models.CharField(max_length=100, null=True)
    address_manager = models.CharField(max_length=100, null=True)
    addressable_object_id = models.IntegerField(null=True)
    address_class = models.CharField(max_length=100, null=True)
    parcel_id = models.IntegerField(null=True, db_index=True)


class TitleParcel(models.Model):
    # title_id = id
    title_no = models.CharField(max_length=100, null=True, db_index=True)
    par_id = models.IntegerField(null=True)
    source = models.CharField(max_length=100, null=True)


class StreetAddress(models.Model):
    WKT = models.TextField(null=True)
    # address_id = id
    change_id = models.IntegerField(null=True)
    address_type = models.CharField(max_length=100, null=True)
    unit_value = models.CharField(max_length=100, null=True)
    address_number = models.CharField(max_length=100, null=True)
    address_number_suffix = models.CharField(max_length=100, null=True)
    address_number_high = models.CharField(max_length=100, null=True)
    water_route_name = models.CharField(max_length=1000, null=True)
    water_name = models.CharField(max_length=1000, null=True)
    suburb_locality = models.CharField(max_length=100, null=True)
    town_city = models.CharField(max_length=100, null=True)
    full_address_number = models.CharField(max_length=100, null=True)
    full_road_name = models.CharField(max_length=1000, null=True)
    full_address = models.CharField(max_length=1000, null=True)
    road_section_id = models.IntegerField(null=True)
    gd2000_xcoord = models.FloatField(null=True)
    gd2000_ycoord = models.FloatField(null=True)
    water_route_name_ascii = models.CharField(max_length=1000, null=True)
    water_name_ascii = models.CharField(max_length=1000, null=True)
    suburb_locality_ascii = models.CharField(max_length=1000, null=True)
    town_city_ascii = models.CharField(max_length=1000, null=True)
    full_road_name_ascii = models.CharField(max_length=1000, null=True)
    full_address_ascii = models.CharField(max_length=1000, null=True)
    shape_X = models.FloatField(null=True)
    shape_Y = models.FloatField(null=True)


class AddressTitle(models.Model):
    # title_id = id
    title_no = models.CharField(max_length=191, null=True, db_index=True)
    full_address = models.CharField(max_length=191, null=True)
    address = models.CharField(max_length=191, null=True)
    suburb = models.CharField(max_length=100, null=True)


class AddressTitleMortgageOwner(models.Model):
    title_no = models.CharField(max_length=191, null=True, db_index=True)
    encumbrancees = models.CharField(max_length=1000, null=True)
    instrument_lodged_datetime = models.DateTimeField(null=True)
    instrument_type = models.CharField(max_length=191, null=True)
    full_address = models.CharField(max_length=191, null=True)
    address = models.CharField(max_length=191, null=True, db_index=True)
    suburb = models.CharField(max_length=191, null=True)
    estate_description = models.TextField(max_length=1000, null=True)
    owners = models.CharField(max_length=10000, null=True)
    issue_date = models.DateTimeField(null=True)
    type = models.CharField(max_length=191, null=True)
    land_district = models.CharField(max_length=191, null=True)


class OwnerTitleAddress(models.Model):
    title_no = models.CharField(max_length=191, null=True, db_index=True)
    land_district = models.CharField(max_length=191, null=True)
    instrument_lodged_datetime = models.DateTimeField(null=True)
    issue_date = models.DateTimeField(null=True)
    owner = models.CharField(max_length=191, null=True, db_index=True)
    full_address = models.CharField(max_length=191, null=True)
    address = models.CharField(max_length=191, null=True, db_index=True)
