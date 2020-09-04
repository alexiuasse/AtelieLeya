#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:08.

# users/forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        widgets = {
            'birth_day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ('username', 'email', 'birth_day', 'whatsapp')


class CustomUserChangeFrontendForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeFrontendForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nome"

    class Meta:
        model = CustomUser
        widgets = {
            'birth_day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ('username', 'whatsapp', 'first_name', 'last_name', 'birth_day', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        widgets = {
            'birth_day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
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
        widgets = {
            'birth_day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ('username', 'whatsapp', 'first_name', 'birth_day', 'email', 'password1', 'password2',)


class RewardRetrievedForm(forms.ModelForm):
    prefix = "rewardretrieved"

    layout = Layout(
        Row(
            Field('reward', wrapper_class='col-md'),
            # Field('quantity', wrapper_class='col-md'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'

    class Meta:
        model = RewardRetrieved
        fields = ['reward']
