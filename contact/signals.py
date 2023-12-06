from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from contact.models import Contact


@receiver(post_save, sender=Contact)
def message_replied(instance, created, update_fields, **kwargs):
    if not created and 'reply' in update_fields:
        instance.replied = True
        _send_email(
            subject='Sua mensagem foi respondida!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipients=(instance.email, settings.DEFAULT_FROM_EMAIL),
            template_name='contact/contact_response.txt',
            context={'response': instance},
        )


def _send_email(subject, from_email, recipients, template_name, context):
    message = render_to_string(template_name, context)
    mail.send_mail(subject, message, from_email, recipients)
