from datetime import datetime

from django.test import TestCase

from contact.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.data = Contact(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-91234-5678',
            message='Lorem ipsum dolor sit amet',
        )
        self.data.save()

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.data.created_at, datetime)

    def test_replied_default_false(self):
        self.assertFalse(self.data.replied)

    def test_str(self):
        self.assertEqual(str(self.data), 'Pedro Machado')
