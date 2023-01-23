from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from eventex.subscriptions.models import Subscription

class Subscribe_Get(TestCase):
    
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
    
    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
    
    def test_html(self):
        tags = (('<form',1),
                ('<input',6),
                ('type="text"',3),
                ('type="email"',1),
                ('type="submit"',1))
        
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
    
    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
    
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
class Subscribe_Post_Valid(TestCase):
    def setUp(self):
        data = dict(nome = "Henrique Bastos", CPF = "12345678901", 
            email = "henrique@bastos.net", telefone = "21-99150-5625")
        self.resp = self.client.post("/inscricao/", data)
    
    def test_post(self):
        self.assertEqual(302, self.resp.status_code)
    
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())

class Subscribe_Post_Invalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
    
    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
    
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)
    
    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

class Subscribe_Sucess_Message(TestCase):
    def test_message(self):
        data = dict(nome='Henrique Bastos', CPF='12345678901', 
                    email='henrique@bastos.net', telefone='21-99150-5625')
        resp = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(resp, 'Inscrição realizada com sucesso!')