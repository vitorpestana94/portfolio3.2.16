from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class Subscription_Form_Test(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()
    
    def test_form_has_field(self):
        expected = ['nome', 'CPF', 'email', 'telefone']
        self.assertSequenceEqual(expected, list(self.form.fields))