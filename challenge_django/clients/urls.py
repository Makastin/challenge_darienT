## Djago Packages ##

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path


## VIEWS CLIENT APP ##
from clients.views import (
        ClientCreate, 
        ClientDelet, 
        ClientDetail, 
        ClientList,
        ClientUpdate,
        ClientTypeCreate
)

urlpatterns = [
    re_path('create-client/$',
            login_required(ClientCreate.as_view()), name="client-create"),                      ## URL CLIENT CREATE
    path('detail-client/<int:pk>/',
            login_required(ClientDetail.as_view()), name="client-detail"),                      ## URL CLIENT DETAIL
    path('update-client/<int:pk>/',
            login_required(ClientUpdate.as_view()), name="client-update"),                      ## URL CLIENT UPDATE
    re_path('list-client/$',
            login_required(ClientList.as_view()), name="client-list"),                          ## URL CLIENT LIST
    path('delet-client/<int:pk>/',
            login_required(ClientDelet.as_view()), name="client-delet"),                        ## URL CLIENT DELETE
    re_path('create-client-type/$',
            login_required(ClientTypeCreate.as_view()), name="client-type-create"),             ## URL CLIENTTYPE CREATE
]
