from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from clients.views import ClientCreate, ClientDetail, ClientUpdate, ClientList, ClientDelet

urlpatterns = [
    re_path('create-client/$',
            login_required(ClientCreate.as_view()), name="client-create"),      ## URL CLIENT CREATE
    path('detail-client/<int:pk>/',
            login_required(ClientDetail.as_view()), name="client-detail"),      ## URL CLIENT DETAIL
    path('update-client/<int:pk>/',
            login_required(ClientUpdate.as_view()), name="client-update"),      ## URL CLIENT UPDATE
    re_path('list-client/$',
            login_required(ClientList.as_view()), name="client-list"),          ## URL CLIENT LIST
    path('delet-client/<int:pk>/',
            login_required(ClientDelet.as_view()), name="client-delet"),        ## URL CLIENT DELETE
    
]