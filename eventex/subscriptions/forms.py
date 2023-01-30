from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve conter apenas 11 números.', 'length')
class SubscriptionForm(forms.Form):
    nome = forms.CharField(label="Nome:")
    CPF = forms.CharField(label="CPF:", validators = [validate_cpf])
    email = forms.EmailField(label="Email:")
    telefone = forms.CharField(label="Telefone:")