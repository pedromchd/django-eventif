from django.apps import AppConfig


class ContactMessagesConfig(AppConfig):
    name = 'contact'
    verbose_name = 'Controle de Mensagens'

    def ready(self):
        import contact.signals
