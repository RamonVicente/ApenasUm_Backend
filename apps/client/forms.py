from django import forms
from allauth.account.forms import SignupForm

from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'cpf', 'email', 'telefone']

    def __init__(self,*args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        # GENERAL INFO
        self.fields['nome_completo'].widget.attrs['class'] = 'form-control'
        self.fields['nome_completo'].widget.attrs['placeholder'] = 'Nome Completo'

        self.fields['cpf'].widget.attrs['class'] = 'form-control masked-cpf'
        self.fields['cpf'].widget.attrs['placeholder'] = 'CPF'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['telefone'].widget.attrs['class'] = 'form-control masked-phone'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone'
