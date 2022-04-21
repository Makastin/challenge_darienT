 ## Django packages ##

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from credits.models import Credits, CreditType
from credits.forms import CreditsForm
from django.urls import reverse_lazy

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

