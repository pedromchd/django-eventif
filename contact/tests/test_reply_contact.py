from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase

from contact.models import Contact


class ContactEmailTest(TestCase):
    def setUp(self):
        self.data = Contact.objects.create(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-91234-5678',
            message='Lorem ipsum dolor sit amet',
        )
        self.data.reply = 'Consectetur adipiscing elit'
        self.data.save(update_fields=['reply'])
        self.email = mail.outbox[0]

    def test_contact_replied(self):
        self.assertTrue(self.data.replied)

    def test_email_subject(self):
        expect = 'Sua mensagem foi respondida!'
        self.assertEqual(self.email.subject, expect)

    def test_email_sender(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(self.email.from_email, expect)

    def test_email_recipients(self):
        expect = ['pedro.machado@mail.com', 'contato@eventif.com.br']
        self.assertEqual(self.email.to, expect)

    def test_email_message(self):
        contents = (
            'Pedro Machado',
            'pedro.machado@mail.com',
            '053-91234-5678',
            'Lorem ipsum dolor sit amet',
            'Consectetur adipiscing elit',
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
