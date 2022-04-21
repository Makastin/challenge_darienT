from django.db import models


class BankType(models.Model):
    bank_type = models.CharField(
        verbose_name = 'Bank Type',
        max_length = 11
    )
    
    class Meta:
        verbose_name = 'Bank Type'
        verbose_name_plural = 'Bank Types'

    def __str__(self):
        return self.bank_type


class Bank(models.Model):
    name = models.CharField(
        verbose_name = 'Bank Name',
        max_length = 150
    )
    bank_type = models.ForeignKey(
        BankType, 
        on_delete=models.CASCADE,
        verbose_name = 'Bank Type',
    )
    address = models.CharField(
        verbose_name = 'Bank Address',
        max_length = 150
    )
    allowed_credit = models.BooleanField(
        'Allowed Credit',
        default = False
    )
    
    
    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'

    def __str__(self):
        return self.name