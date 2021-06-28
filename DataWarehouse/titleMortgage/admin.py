from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome"

class TitleMortgagePageAdmin(admin.ModelAdmin):
    list_display = ['title_no', 'encumbrancees', 'instrument_lodged_datetime', 'instrument_type', 'memorial_text']
    # list_filter = [
    #     'encumbrancees'
    # ]
    search_fields = [
        'instrument_type',
        'encumbrancees'
    ]
    # ordering = ['-instrument_lodged_datetime']

admin.site.register(TitleMortgage, TitleMortgagePageAdmin)
