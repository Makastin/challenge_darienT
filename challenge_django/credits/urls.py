 ## Django packages ##

from credits.views import CreditDetail, CreditList, CreditsCreate, CreditTypeCreate
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

 ## URLS OF CREDITS APP ##
urlpatterns = [
    re_path('create-credits/$',
            login_required(CreditsCreate.as_view()), name="credit-create"),             ## URL CREDIT CREATE
    path('detail-credit/<int:pk>/',
            login_required(CreditDetail.as_view()), name="credit-detail"),              ## URL CREDIT DETAIL
    re_path('list-credits/$',
            login_required(CreditList.as_view()), name="credit-list"),                  ## URL CREDITS LIST
    re_path('create-credits-type/$',
            login_required(CreditTypeCreate.as_view()), name="credit-type-create"),     ## URL CREDITTYPE CREATE
    
]