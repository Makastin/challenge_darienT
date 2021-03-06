## Django Package ##

## MODELS CLIENT APP ##
from clients.models import Client, ClientType
from django.forms import ModelForm
from django.forms.widgets import DateInput, EmailInput, NumberInput, Select, TextInput


## CLIENT CREATEFORM ##
class ClientFormCreate(ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'age',
            'nationality',
            'address',
            'email',
            'phone_number',
            'client_type',
            'bank_entity',
            
        ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'birth_date': DateInput(attrs={'class': 'form-control', 'required': 'True'}),
            'age': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'nationality': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'address': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'True'}),
            'phone_number': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'client_type': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'bank_entity': Select(attrs={'class': 'form-control', 'required': 'True'}),
        }


## CLIENT UPDATEFORM ##
class ClientFormUpdate(ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'age',
            'nationality',
            'address',
            'email',
            'phone_number',
            'client_type',
            'bank_entity',
            
        ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'birth_date': DateInput(attrs={'class': 'form-control', 'required': 'True'}),
            'age': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'nationality': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'address': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'True'}),
            'phone_number': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'client_type': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'bank_entity': Select(attrs={'class': 'form-control', 'required': 'True'}),
        }


## CLIENTTYPE CREATEFORM ##
class ClientTypeForm(ModelForm):
    class Meta:
        model = ClientType
        fields = [
            'client_type',
        ]
        widgets = {
            'client_type': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
        }