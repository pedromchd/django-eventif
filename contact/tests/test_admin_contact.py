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
