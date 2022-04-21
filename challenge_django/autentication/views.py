 ## Django packages ##

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


## Login View ##
class LoginView(LoginView):
    template_name = 'login/login.html'
    success_url = success_url = reverse_lazy('home')

## Home View ##
class Home(TemplateView):
    template_name = "home/home.html"