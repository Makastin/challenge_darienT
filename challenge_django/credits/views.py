 ## Django packages ##

from credits.forms import CreditsForm, CreditTypeForm
from credits.models import Credits, CreditType
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView


 ## CREATEVIEW OF MODEL CREDIT ##
class CreditsCreate(CreateView):
    model = Credits
    form_class = CreditsForm
    template_name = "credits/credit_create.html"
    success_url = reverse_lazy('credits:credit-list')
    
    def form_valid(self, form):
        return super().form_valid(form)


 ## DETAILVIEW OF MODEL CREDIT ##
class CreditDetail(DetailView):
    model = Credits
    template_name = "credits/credit_detail.html"


## LIST OF MODEL CREDITS ##
class CreditList(TemplateView):
    template_name = "credits/credit_list.html"
    
    def get(self, request, *args, **kwargs):
        credits_list = Credits.objects.prefetch_related('client', 'bank_of_credit' ).distinct()
        context = {'credits_list': credits_list}
        return self.render_to_response(context)
    
    
 ## CREATEVIEW OF MODEL CREDITTYPE ##
class CreditTypeCreate(CreateView):
    model = CreditType
    form_class = CreditTypeForm
    template_name = "credits/credit_type_create.html"
    success_url = reverse_lazy('credits:credit-create')
    
    def form_valid(self, form):
        return super().form_valid(form)

