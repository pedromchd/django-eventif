from unittest.mock import Mock

from django.test import TestCase

from contact.admin import ContactModelAdmin, Contact, admin


class ContactModelAdminTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-91234-5678',
            message='Lorem ipsum dolor sit amet',
        )

        self.model_admin = ContactModelAdmin(Contact, admin.site)

    def test_has_action(self):
        self.assertIn('mark_as_replied', self.model_admin.actions)

    def test_mark_all(self):
        self.call_action()
        self.assertEqual(Contact.objects.filter(replied=True).count(), 1)

    def test_message(self):
        self.call_action()
        self.mock.assert_called_once_with(
            None, '1 mensagem foi marcada como respondida'
        )

    def call_action(self):
        queryset = Contact.objects.all()

        self.mock = Mock()
        old_message_user = ContactModelAdmin.message_user

        ContactModelAdmin.message_user = self.mock

        self.model_admin.mark_as_replied(None, queryset)

        ContactModelAdmin.message_user = old_message_user
