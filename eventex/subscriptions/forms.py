from django import forms

class SubscriptionForm(forms.Form):
    nome = forms.CharField(label="Nome:")
    CPF = forms.CharField(label="CPF:")
    email = forms.EmailField(label="Email:")
    telefone = forms.CharField(label="Telefone:")