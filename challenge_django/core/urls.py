from django.contrib import admin
from django.urls import path, include
from autentication.views import LoginView, Home
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
    ),
    path(
        '', 
    LoginView.as_view(),
    name='login'
    ),
    path(
        'logout/',
        logout_then_login, 
        name="logout",
    ),
    path(
        'home/', 
        login_required(Home.as_view()), 
        name="home"
    ),
    path(
        'clients/', 
        include(
            (
                'clients.urls', 
                'clients'
            ), 
        namespace='clients'
        )
    ),
    path(
        'banks/', 
        include(
            (
                'banks.urls', 
                'banks'
            ), 
        namespace='banks'
        )
    ),
    path(
        'credits/', 
        include(
            (
                'credits.urls', 
                'credits'
            ), 
        namespace='credits'
        )
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)