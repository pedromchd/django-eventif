from django.test import TestCase

from contact.forms import ContactForm


class ContactFormTest(TestCase):
    def test_form_has_fields(self):
        form = ContactForm()
        self.assertTupleEqual(tuple(form.fields), ('name', 'email', 'phone', 'message'))

    def test_name_must_be_capitalized(self):
        form = self.make_validated_form(name='PEDRO machado')
        self.assertEqual(form.cleaned_data['name'], 'Pedro Machado')

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_phone_empty_value(self):
        form = self.make_validated_form(phone='')
        self.assertEqual(form.cleaned_data['phone'], 'Não informado')

    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-91234-5678',
            message='Lorem ipsum dolor sit amet',
        )
        data = dict(valid, **kwargs)
        form = ContactForm(data)
        form.is_valid()
        return form
