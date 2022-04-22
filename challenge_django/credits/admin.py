 ## Django packages ##

from credits.models import Credits, CreditType
from django.contrib import admin


 ## ADMIN VIEW OF CREDITS MODEL ##
@admin.register(Credits)
class CreditsAdmin(admin.ModelAdmin):

    list_display = (
        'client',
        'bank_of_credit',
        'created_at'
    )
    list_filter = (
        'client',
        'bank_of_credit',
        'created_at'
    )
    search_fields = (
        'client__first_name',
        'client__last_name',
        'bank_of_credit__name'
    )



 ## ADMIN VIEW OF CREDIT TYPES ##    
@admin.register(CreditType)
class CreditTypeAdmin(admin.ModelAdmin):
    search_fields = ['credit_type']