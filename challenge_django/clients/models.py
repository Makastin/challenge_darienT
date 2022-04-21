from django.db import models
from banks.models import Bank


class ClientType(models.Model):
    client_type = models.CharField(
        verbose_name = 'Client Type',
        max_length = 15
    )
    
    class Meta:
        verbose_name = 'Client Type'
        verbose_name_plural = 'Client Types'

    def __str__(self):
        return self.client_type


class Client(models.Model):
    first_name = models.CharField(
        verbose_name = 'First Name',
        max_length = 10
    )
    last_name = models.CharField(
        verbose_name = 'Last Name',
        max_length = 15
    )
    birth_date = models.DateField(
        verbose_name = 'Birth Date'
    )
    age = models.IntegerField(
        verbose_name = 'Age',
        blank = True,
        null = True
    )
    nationality = models.CharField(
        verbose_name = 'Nationality',
        max_length = 15,
        blank = True,
        null = True
    )
    address = models.CharField(
        verbose_name = 'Address',
        max_length = 50,
        blank = True,
        null = True
    )
    email = models.EmailField(
        verbose_name = 'Email account',
        max_length= 80
    )
    phone_number = models.CharField(
        verbose_name = 'Phone Number',
        max_length = 13,
        blank = True,
        null = True
    )
    client_type = models.ForeignKey(
        ClientType, 
        on_delete=models.CASCADE,
        verbose_name = 'Client Type',
        blank = True,
        null = True
    )
    bank_entity = models.ForeignKey(
        Bank, 
        on_delete=models.CASCADE,
        verbose_name = 'Bank Entity',
        blank = True,
        null = True
    )
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)