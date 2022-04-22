 ## Django packages ##

from django.db import models
from clients.models import Client
from banks.models import Bank



 ## MODEL OF CREDIT TYPES ##
class CreditType(models.Model):
    credit_type = models.CharField(
        verbose_name = 'Credit Type',
        max_length = 15,
    )
    
    
    class Meta:
        verbose_name = 'Credit Type'
        verbose_name_plural = 'Credit Types'

    def __str__(self):
        return self.credit_type


 ## MODEL OF CREDITS ##
class Credits(models.Model):
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE,
        verbose_name = 'Client'
    )
    credit_description = models.CharField(
        verbose_name = 'Credit Description',
        max_length = 150
    )
    min_payment = models.DecimalField(
        verbose_name = 'Minimum Payment',
        max_digits=10,
        decimal_places=2
    )
    max_payment = models.DecimalField(
        verbose_name = 'Maximun Payment',
        max_digits=10,
        decimal_places=2
    )
    credit_term = models.PositiveIntegerField(
        verbose_name = 'Credit Term',
    )
    bank_of_credit = models.ForeignKey(
        Bank, 
        on_delete=models.CASCADE,
        limit_choices_to= {'allowed_credit':True},   
        verbose_name = 'Bank of Credit'
    )
    credit_type = models.ForeignKey(
        CreditType, 
        on_delete=models.CASCADE,
        verbose_name='Credit Type',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    
    class Meta:
        verbose_name = 'Credit'
        verbose_name_plural = 'Credits'

    def __str__(self):
        return "%s - %s" % (self.client, self.bank_of_credit)
