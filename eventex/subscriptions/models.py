from django.db import models

class Subscription(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)