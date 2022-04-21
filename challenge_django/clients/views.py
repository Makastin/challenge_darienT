from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, DeleteView
from clients.models import Client
from clients.forms import ClientFormCreate, ClientFormUpdate
from django.urls import reverse_lazy


class ClientCreate(CreateView):
    model = Client
    form_class = ClientFormCreate
    template_name = 'clients/client_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        return super().form_valid(form)

    
class ClientDetail(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
    
class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientFormUpdate
    template_name = 'clients/client_update.html'
    success_url = reverse_lazy('clients:client-list')
    
    def form_valid(self, form):
        return super().form_valid(form)


class ClientDelet(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client-list')

class ClientList(TemplateView):
   template_name = 'clients/client_list.html'
   
   def get(self, request, *args, **kwargs):
        client_list = Client.objects.prefetch_related('client_type', 'bank_entity').distinct()
        context = {'client_list': client_list}
        return self.render_to_response(context)
