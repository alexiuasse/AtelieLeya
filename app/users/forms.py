#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 19:08.

# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'birth_day', 'whatsapp')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    whatsapp = forms.CharField(label="Whatsapp", max_length=16, required=True, help_text='Seu número com whatsapp.')
    first_name = forms.CharField(label="Nome", max_length=30, required=True, help_text='Obrigatório.')
    # last_name = forms.CharField(label="Último Nome", max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(label="E-mail", max_length=254, help_text='Informe um endereço de e-mail válido')
    birth_day = forms.DateField(label="Data de Nascimento", widget=DateInput, help_text='Informe uma data válida')

    class Meta:
        model = CustomUser
        fields = ('username', 'whatsapp', 'first_name', 'birth_day', 'email', 'password1', 'password2',)
