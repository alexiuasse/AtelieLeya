#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/09/2020 12:37.

# users/forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import *


class UserChangeFormFrontend(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('email',)


class UserCreationFormFrontend(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileFormFrontend(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'birth_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ('name', 'whatsapp', 'birth_date')


class ProfileFormAdmin(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'birth_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ('name', 'whatsapp', 'birth_date', 'total_of_points')


class RewardRetrievedForm(forms.ModelForm):
    prefix = "rewardretrieved"

    layout = Layout(
        Row(
            Field('reward', wrapper_class='col-md-12'),
            Field('retrieved', wrapper_class='col-md-12 mt-2'),
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
        fields = ['reward', 'retrieved']
