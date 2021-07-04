from django.contrib import admin
from .models import *
from django.forms import ModelForm, Form
from django.forms import DateField, CharField, ChoiceField, TextInput
from django_admin_search.admin import AdvancedSearchAdmin

# Register your models here.

remove_fields = ['suburb', 'address']


class FormSearchMortgage(Form):
    encumbrancees = CharField(required=False, widget=TextInput(
        attrs={
            'filter_field': 'encumbrancees',
            'filter_method': '__icontains'
        }
    ))
    address = CharField(required=False, widget=TextInput(
        attrs={
            'filter_field': 'address',
            'filter_method': '__icontains'
        }
    ))
    title_no = CharField(required=False)


class AddressTitleMortgageOwnerPageAdmin(admin.ModelAdmin):
    list_display = [field.name for field
                    in AddressTitleMortgageOwner._meta.get_fields() if field.name not in remove_fields]
    # search_form = FormSearchMortgage
    search_fields = [
        'encumbrancees',
        'title_no',
        'address'
    ]


class FormSearchOwner(Form):
    address = CharField(required=False, widget=TextInput(
        attrs={
            'filter_field': 'address',
            'filter_method': '__icontains'
        }
    ))
    title_no = CharField(required=False)
    owner = CharField(required=False)


class OwnerVSTitleVSAddressAdmin(AdvancedSearchAdmin):
    list_display = [field.name for field in OwnerTitleAddress._meta.get_fields()]
    search_form = FormSearchOwner
    # search_fields = [
    #     'address',
    #     'title_no',
    #     'owner'
    # ]


admin.site.register(AddressTitleMortgageOwner, AddressTitleMortgageOwnerPageAdmin)
admin.site.register(OwnerTitleAddress, OwnerVSTitleVSAddressAdmin)
