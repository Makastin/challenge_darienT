 ## Django packages ##

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path


## MODEL BANK APP ##
from banks.views import BankCreate, BankDetail, BankList, BankTypeCreate

 ## URLS BANK APP ##

urlpatterns = [
    re_path('create-bank/$',
            login_required(BankCreate.as_view()), name="bank-create"),              ## URL BANK CREATE ##
    path('detail-bank/<int:pk>/',
            login_required(BankDetail.as_view()), name="bank-detail"),              ## URL BANK DETAIL ##
    re_path('list-banks/$',
            login_required(BankList.as_view()), name="bank-list"),                  ## URL BANK LIST
    re_path('create-bank-type/$',
            login_required(BankTypeCreate.as_view()), name="bank-type-create"),     ## URL BANK TYPE
    
]
