from django.contrib import admin
from .models import *

# Register your models here.
remove_fields = ['suburb', 'address']


class AddressTitleMortgageOwnerPageAdmin(admin.ModelAdmin):
    list_display = [field.name for field
                    in AddressTitleMortgageOwner._meta.get_fields() if field.name not in remove_fields]
    # list_filter = [
    #     'suburb',
    #     'type'
    # ]
    search_fields = [
        'title_no',
        'encumbrancees',
        'address'

    ]
    # ordering = ['-instrument_lodged_datetime']


class OwnerVSTitleVSAddressDdmin(admin.ModelAdmin):
    list_display = [field.name for field in OwnerTitleAddress._meta.get_fields()]
    # list_filter = [
    #     'suburb',
    #     'type'
    # ]
    search_fields = [
        'title_no',
        'owner',
        'address'

    ]
    # ordering = ['-instrument_lodged_datetime']


admin.site.register(AddressTitleMortgageOwner, AddressTitleMortgageOwnerPageAdmin)
admin.site.register(OwnerTitleAddress, OwnerVSTitleVSAddressDdmin)
