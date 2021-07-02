from django.contrib import admin
from .models import *
from django.forms import ModelForm, Form
from django.forms import DateField, CharField, ChoiceField, TextInput
from django_admin_search.admin import AdvancedSearchAdmin

# Register your models here.
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome"


class FormSearchMortgage(Form):
    encumbrancees = CharField(required=False, widget=TextInput(
        attrs={
            'filter_field': 'encumbrancees',
            'filter_method': '__icontains'
        }
    ))
    instrument_type = CharField(required=False)
    title_no = CharField(required=False)


class TitleMortgagePageAdmin(admin.ModelAdmin):
    list_display = ['title_no', 'encumbrancees', 'instrument_lodged_datetime', 'instrument_type', 'memorial_text']

    search_fields = [
        'title_no',
        'instrument_type',
        'encumbrancees'
    ]
    # search_form = FormSearchMortgage
    # ordering = ['-instrument_lodged_datetime']


admin.site.register(TitleMortgage, TitleMortgagePageAdmin)
