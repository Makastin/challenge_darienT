 ## Django packages ##

from credits.models import Credits, CreditType
from django.forms import ModelForm
from django.forms.widgets import (
    CheckboxInput, 
    DateInput, 
    NumberInput,
    Select,
    Textarea,
    TextInput,
    EmailInput,
)

 ## CreationsForm of Model Credit ##
class CreditsForm(ModelForm):
    class Meta:
        model = Credits
        fields =[
            'client',
            'credit_description',
            'min_payment',
            'max_payment',
            'credit_term',
            'bank_of_credit',
        ]
        widgets = {
            'min_payment': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'max_payment': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'credit_term': NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'bank_of_credit': Select(attrs={'class': 'form-control', 'required': 'True'}),
            'credit_description': TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'client': Select(attrs={'class': 'form-control', 'required': 'True'}),
        }