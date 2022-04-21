 ## Django packages ##

from django.shortcuts import render
from banks.models import Bank, BankType
from banks.forms import BankCreateForm, BankTypeCreateForm
from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse_lazy



 ## CREATEVIEW OF MODEL BANK ##
class BankCreate(CreateView):
    model = Bank
    form_class = BankCreateForm
    template_name = "banks/bank_create.html"
    success_url = reverse_lazy('banks:bank-list')
    
    def form_valid(self, form):
        return super().form_valid(form)


## LIST OF ALL BANKS CREATED ##
class BankList(TemplateView):
   template_name = 'banks/bank_list.html'
   
   def get(self, request, *args, **kwargs):
        bank_list = Bank.objects.prefetch_related('bank_type').distinct()
        context = {'bank_list': bank_list}
        return self.render_to_response(context)
    

 ## DETAILVIEW OF BANKS ##    
class BankDetail(DetailView):
    model = Bank
    template_name = "banks/bank_detail.html"


 ## CREATEVIEW OF BANKTYPES ##
class BankTypeCreate(CreateView):
    model = BankType
    template_name = "banks/bank_type_create.html"
    

