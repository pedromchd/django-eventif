from django.test import TestCase

class TestViewContact(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_view_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_extends_base(self):
        self.assertTemplateUsed(self.response, 'base.html')

    def test_view_uses_contact_form(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')
