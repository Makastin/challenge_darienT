from django.contrib import admin
from credits.models import Credits, CreditType

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
    
@admin.register(CreditType)
class CreditTypeAdmin(admin.ModelAdmin):
    search_fields = ['credit_type']