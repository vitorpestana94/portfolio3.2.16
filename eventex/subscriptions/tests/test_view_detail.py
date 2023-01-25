from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            nome = 'Henrique Bastos', 
            CPF ='12345678901',
            email ='henrique@bastos.net',
            telefone = '21-99150-5625')
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp,
                    'subscriptions/subscription_detail.html')
    
    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)
    
    def test_html(self):
        contents = (self.obj.nome, self.obj.CPF,
                    self.obj.CPF, self.obj.telefone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)

class SubscriptionNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('inscricao/0/')
        self.assertEqual(404, resp.status_code)