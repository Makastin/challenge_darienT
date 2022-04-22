## Django Packages ##

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DeleteView, 
    DetailView,
    TemplateView, 
    UpdateView
)


## MODEL AND FORM CLIENT APP ##
from clients.forms import ClientFormCreate, ClientFormUpdate
from clients.models import Client


## CREATEVIEW MODEL CLIENT ##
class ClientCreate(CreateView):
    model = Client
    form_class = ClientFormCreate
    template_name = 'clients/client_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        return super().form_valid(form)


## DETAILVUEW MODEL CLIENT ##
class ClientDetail(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
    

## UPDATEVIEW MODEL CLIENT ##
class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientFormUpdate
    template_name = 'clients/client_update.html'
    success_url = reverse_lazy('clients:client-list')
    
    def form_valid(self, form):
        return super().form_valid(form)


## DELETEVIEW MODEL CLIENT
class ClientDelet(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client-list')


## LIST OF MODEL CLIENT ##
class ClientList(TemplateView):
    template_name = 'clients/client_list.html'
    
    def get(self, request, *args, **kwargs):
        client_list = Client.objects.prefetch_related('client_type', 'bank_entity').distinct()
        context = {'client_list': client_list}
        return self.render_to_response(context)
