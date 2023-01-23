from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelTest (TestCase):
    def setUp(self):
        self.obj = Subscription(
            nome='Henrique Bastos',
            CPF = '12345678901',
            email = 'henrique@bastos.net',
            telefone = '21-99150-5625'
        )
        
        self.obj.save()
    
    def test_create (self):
        self.assertTrue(Subscription.objects.exists())
    
    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual("Henrique Bastos", str(self.obj))