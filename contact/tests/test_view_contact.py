from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase

from contact.forms import ContactForm


class ContactFormTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('contact'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    def test_form_has_fields(self):
        form = ContactForm()
        self.assertTupleEqual(tuple(form.fields), ('name', 'email', 'phone', 'message'))

    def test_has_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ContactForm)

    def test_form_tags(self):
        tags = (('<form', 1), ('<input', 5), ('<textarea', 1))
        for tag, count in tags:
            with self.subTest():
                self.assertContains(self.response, tag, count)

    def test_input_attributes(self):
        attribs = (
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1),
            ('type="hidden"', 1),
        )
        for attrib, count in attribs:
            with self.subTest():
                self.assertContains(self.response, attrib, count)

    def test_form_has_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class ContactPostValidTest(TestCase):
    def setUp(self):
        data = dict(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-98429-5133',
            message='Lorem ipsum dolor sit amet',
        )
        self.response = self.client.post(r('contact'), data)

    def test_post_success(self):
        self.assertEqual(self.response.status_code, 302)

    def test_email_sent(self):
        self.assertTrue(mail.outbox)


class TestPostInvalid(TestCase):
    def setUp(self):
        data = {}
        self.response = self.client.post(r('contact'), data, follow=True)

    def test_redirect_back(self):
        self.assertEqual(self.response.status_code, 200)

    def test_has_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
