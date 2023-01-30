from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class Subscription_Form_Test(TestCase):
    def test_form_has_field(self):
        form = SubscriptionForm()
        expected = ['nome', 'CPF', 'email', 'telefone']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_cpf_is_digit(self):
        form = self.make_validated_form(CPF='ABC45678901')
        self.assertFormErrorCode(form, 'CPF', 'digits')
    
    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(CPF='1234')
        self.assertFormErrorCode(form, 'CPF', 'length')
    
    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)
    
    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)
    
    def make_validated_form(self, **kwargs):
        valid = dict(nome='Henrique Bastos',
                    CPF = '12345678901',
                    email = 'henrique@bastos.net',
                    telefone = '21-99150-5625')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
