from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/inscricao/')
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')
    
    def test_html(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')
    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    def test_form_has_field(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['nome', 'CPF', 'email', 'telefone'], list(form.fields))