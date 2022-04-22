from django.db.models.signals import post_save
from django.dispatch import receiver
from credits.models import Credits
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail



def email_structure(instance, template):
    
    params = {
        'client': instance.client,
        'credit_type': instance.credit_type,
        'bank': instance.bank_of_credit
    }
    
    template = render_to_string(template, params)
    send_mail(
        'Credito Aprobado!',
        '',
        'Tu Credito', [
            instance.client.email
        ], 
        fail_silently=False,
        html_message = template
    )


@receiver(post_save, sender = Credits)
def send_email(sender, instance, created, *args, **kwargs):
   if created:
       email_structure(instance, 'email_template/email.txt')
