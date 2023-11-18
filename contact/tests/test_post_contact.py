from django.core import mail
from django.test import TestCase


class TestPostValid(TestCase):
    def setUp(self):
        data = dict(
            name='Fulano de Tal',
            email='fulano.tal@mail.com',
            message='Olá mundo!',
        )
        self.response = self.client.post('/contato/', data)

    def test_post_status_code_302(self):
        self.assertEqual(self.response.status_code, 302)

    def test_send_contact_mail(self):
        self.assertTrue(mail.outbox)


class TestMailSend(TestCase):
    def setUp(self):
        data = dict(
            name='Fulano de Tal',
            email='fulano.tal@mail.com',
            phone='53912345678',
            message='Olá mundo!',
        )
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_mail_subject(self):
        expect = 'Nova mensagem de Fulano de Tal'
        self.assertEqual(self.email.subject, expect)

    def test_mail_sender(self):
        expect = 'fulano.tal@mail.com'
        self.assertEqual(self.email.from_email, expect)

    def test_mail_recipients(self):
        expect = ['contato@eventif.com.br', 'fulano.tal@mail.com']
        self.assertEqual(self.email.to, expect)

    def test_mail_message(self):
        contents = ('Fulano de Tal', 'fulano.tal@mail.com', '53912345678', 'Olá mundo!')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)


class TestPostInvalid(TestCase):
    def setUp(self):
        data = {}
        self.response = self.client.post('/contato/', data, follow=True)

    def test_post_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_form_has_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
