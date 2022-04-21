from django.contrib import admin
from clients.models import Client, ClientType

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    
    list_display = (
        'first_name',
        'last_name',
        'email',
        'bank_entity'
    )
    search_fields = (
        'first_name',
        'last_name',
        'email'
    )
    
@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):

    search_fields = ['client_type']