from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        form = SubscriptionForm()
        self.assertSequenceEqual(
            ['name', 'cpf', 'email', 'phone'], list(form.fields))

    def test_cpf_has_digit(self):
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='123456')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        form = self.make_validated_form(name='PEDRO machado')
        self.assertEqual('Pedro Machado', form.cleaned_data['name'])

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_of_phone(self):
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        error_list = errors[field]
        self.assertListEqual([msg], error_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Pedro Machado', cpf='12345678901',
                     email='pedro@mail.com', phone='53-91234-5678')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
