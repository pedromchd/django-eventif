from django.test import TestCase

from contact.forms import ContactForm


class TestFormContact(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_contact_form_has_fields(self):
        form = ContactForm()
        self.assertTupleEqual(tuple(form.fields), ('name', 'email', 'phone', 'message'))

    def test_view_form_inherits_contact_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ContactForm)

    def test_view_form_has_tags(self):
        tags = (('<form', 1), ('<input', 5), ('<textarea', 1))
        for tag, count in tags:
            with self.subTest():
                self.assertContains(self.response, tag, count)

    def test_view_form_inputs_have_attributes(self):
        attribs = (
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1),
            ('type="hidden"', 1),
        )
        for attrib, count in attribs:
            with self.subTest():
                self.assertContains(self.response, attrib, count)

    def test_view_form_has_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
