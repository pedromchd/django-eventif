from django.db.models.signals import post_save
from django.dispatch import receiver

from contact.models import Contact


@receiver(post_save, sender=Contact)
def message_replied(instance, created, update_fields, **kwargs):
    if not created and 'reply' in update_fields:
        print(instance.reply)
