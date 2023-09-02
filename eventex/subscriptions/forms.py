from django import forms
from django.core.exceptions import ValidationError

class SubscriptionForm(forms.Form):
    nome = forms.CharField(label="Nome:")
    email = forms.EmailField(label="Email:")
    telefone = forms.CharField(label="Telefone:")
