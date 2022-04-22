 ## Django packages ##
## MODEL BANK AND CREDITS APP ##
from banks.models import Bank
from clients.models import Client
from credits.models import Credits
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


## Login View ##
class LoginView(LoginView):
    template_name = 'login/login.html'
    success_url = success_url = reverse_lazy('home')


## Home View ##
class Home(TemplateView):
    template_name = "home/home.html"
    
    def get(self, request, *args, **kwargs):
        clients = Client.objects.select_related('client_type', 'bank_entity').distinct().count()
        banks = Bank.objects.select_related('bank_type').distinct().count()
        credits = Credits.objects.select_related('client', 'bank_of_credit').distinct().count()
        
        context = {
            'clients': clients,
            'banks':banks,
            'credits':credits
        }
        return self.render_to_response(context)
