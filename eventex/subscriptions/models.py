from django.db import models

class Subscription(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E_mail')
    telefone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    paid = models.BooleanField('Pago', default=  False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.nome
