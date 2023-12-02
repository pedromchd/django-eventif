from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class ContactEmailTest(TestCase):
    def setUp(self):
        data = dict(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-98429-5133',
            message='Lorem ipsum dolor sit amet',
        )
        self.response = self.client.post(r('contact'), data)
        self.email = mail.outbox[0]

    def test_email_subject(self):
        expect = 'Nova mensagem de Pedro Machado'
        self.assertEqual(self.email.subject, expect)

    def test_email_sender(self):
        expect = 'pedro.machado@mail.com'
        self.assertEqual(self.email.from_email, expect)

    def test_email_recipients(self):
        expect = ['contato@eventif.com.br', 'pedro.machado@mail.com']
        self.assertEqual(self.email.to, expect)

    def test_email_message(self):
        contents = (
            'Pedro Machado',
            'pedro.machado@mail.com',
            '053-98429-5133',
            'Lorem ipsum dolor sit amet',
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
