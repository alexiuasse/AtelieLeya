#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 23/09/2020 10:43.
from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms
from django.forms import TextInput

from .models import *


# REMEMBER: ALWAYS set the fields or the form will not save correctly.


class BaseConfigForm(forms.ModelForm):
    layout = Layout(
        Row(
            Field('name'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'


class TypeOfPaymentForm(BaseConfigForm):
    class Meta:
        model = TypeOfPayment
        fields = ['name']


class RewardForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name'),
            Field('quantity_in_points'),
            Field('contextual'),
            Field('available'),
            Field('description'),
            Field('image'),
        ),
    )

    class Meta:
        model = Reward
        widgets = {
            'contextual': TextInput(attrs={'type': 'color'}),
            # 'image': TextInput(attrs={'type': 'file'}),
            'description': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['name', 'quantity_in_points', 'contextual', 'available', 'description', 'image']


class TypeOfServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name'),
            Field('contextual'),
            PrependedText('value', 'R$'),
            AppendedText('time', 'min'),
            Field('rewarded_points'),
            Field('description'),
            Field('image'),
        ),
    )

    class Meta:
        model = TypeOfService
        widgets = {
            'contextual': TextInput(attrs={'type': 'color'}),
            # 'image': TextInput(attrs={'type': 'file'}),
            'description': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['name', 'contextual', 'value', 'time', 'rewarded_points', 'image', 'description']


class StatusServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name'),
            Field('contextual'),
        ),
    )

    class Meta:
        model = StatusService
        widgets = {
            'contextual': TextInput(attrs={'type': 'color'}),
        }
        fields = ['name', 'contextual']


class StatusPaymentForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name'),
            Field('contextual'),
        ),
    )

    class Meta:
        model = StatusPayment
        widgets = {
            'contextual': TextInput(attrs={'type': 'color'}),
        }
        fields = ['name', 'contextual']


class ExpedientForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name'),
            Field('start_time'),
            Field('end_time'),
        ),
    )

    class Meta:
        model = Expedient
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
        fields = ['name', 'start_time', 'end_time']


class HomePageForm(forms.ModelForm):
    layout = Layout(
        Row(
            Field('address'),
            Field('whatsapp'),
            Field('email'),
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
        model = HomePage
        fields = ['address', 'whatsapp', 'email']
