from django.test import TestCase
from django.core import mail
class Subscribe_Post_Valid(TestCase):
    def setUp(self):
        data = dict(nome = "Henrique Bastos", CPF = "12345678901", 
            email = "henrique@bastos.net", telefone = "21-99150-5625")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
      
    def test_subscription_email_subject(self):
        expect = 'confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Henrique Bastos', 
                    '12345678901',
                    'henrique@bastos.net',
                    '21-99150-5625']
        for content in contents:
            with self.subTest():
                 self.assertIn(content, self.email.body)