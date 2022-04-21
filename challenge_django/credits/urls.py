 ## Django packages ##

from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from credits.views import CreditsCreate, CreditDetail, CreditList


 ## URLS OF CREDITS APP ##
urlpatterns = [
    re_path('create-credits/$',
            login_required(CreditsCreate.as_view()), name="credit-create"),     ## URL CREDIT CREATE
    path('detail-credit/<int:pk>/',
            login_required(CreditDetail.as_view()), name="credit-detail"),      ## URL CREDIT DETAIL
    re_path('list-credits/$',
            login_required(CreditList.as_view()), name="credit-list"),          ## URL CREDITS LIST
    
]