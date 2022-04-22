 ## Django packages ##

from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, Select, TextInput


## MODEL BANK APP ##
from banks.models import Bank, BankType


## CreationForm of Model Bank ##
class BankCreateForm(ModelForm):
    class Meta:
        model = Bank
        fields = [
            'name',
            'bank_type',
            'address',
            'allowed_credit'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'bank_type': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'address': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'allowed_credit': CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        

## CreationForm of Model BankType ##
class BankTypeCreateForm(ModelForm):
    class Meta:
        model = BankType
        fields = [
            'bank_type'
        ]
        widgets = {
            'bank_type': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            }
