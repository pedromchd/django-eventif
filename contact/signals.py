from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from contact.models import Contact
from contact.views import _send_email as send_email


@receiver(post_save, sender=Contact)
def message_replied(instance, created, update_fields, **kwargs):
    if not created and 'reply' in update_fields:
        send_email(
            subject='Sua mensagem foi respondida!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipients=(instance.email, settings.DEFAULT_FROM_EMAIL),
            template_name='contact/contact_response.txt',
            context={'response': instance},
        )
