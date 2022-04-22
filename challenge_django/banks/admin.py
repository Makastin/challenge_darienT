
## Django Packages ##
## MODEL BANK APP ##
from banks.models import Bank, BankType
from django.contrib import admin


## Admin View of Model Bank ##
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'bank_type',
        'address',
        'allowed_credit'
    )
    list_filter = ['allowed_credit']
    search_fields = ['name']
    

## Admin View of Bank Type ##    
@admin.register(BankType)
class BankTypeAdmin(admin.ModelAdmin):

    search_fields = ['bank_type']
    