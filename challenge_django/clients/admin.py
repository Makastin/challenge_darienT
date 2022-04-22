 ## Django packages ##

from django.contrib import admin

from clients.models import Client, ClientType


 ## ADMIN VIEW OF MODEL CLIENT ##
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
    
    
 ## ADMIN VIEW OF MODEL CLIENT TYPE ##
@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):

    search_fields = ['client_type']
