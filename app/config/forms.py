#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/09/2020 13:57.
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
            Field('name', wrapper_class='col-md-12'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.helper.label_class = 'bmd-label-floating'


class TypeOfPaymentForm(BaseConfigForm):
    class Meta:
        model = TypeOfPayment
        fields = ['name']


class RewardForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('quantity_in_points', wrapper_class='col-md-12'),
            Field('contextual', wrapper_class='col-md-12'),
            Field('available', wrapper_class='col-md-12'),
            Field('description', wrapper_class='col-md-12'),
            Field('image', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = Reward
        widgets = {
            'contextual': TextInput(attrs={'type': 'color'}),
            'image': TextInput(attrs={'type': 'file'}),
        }
        fields = ['name', 'quantity_in_points', 'contextual', 'available', 'description', 'image']


class TypeOfServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('contextual', wrapper_class='col-md-12'),
            PrependedText('value', 'R$', wrapper_class='col-md-12'),
            AppendedText('time', 'min', wrapper_class='col-md-12'),
            Field('rewarded_points', wrapper_class='col-md-12'),
            Field('description', wrapper_class='col-md-12'),
            Field('image', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = TypeOfService
        widgets = {
            'contextual': TextInput(attrs={'type': 'color'}),
            # 'image': TextInput(attrs={'type': 'file'}),
        }
        fields = ['name', 'contextual', 'value', 'time', 'rewarded_points', 'image', 'description']


class StatusServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('contextual', wrapper_class='col-md-12'),
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
            Field('name', wrapper_class='col-md-12'),
            Field('contextual', wrapper_class='col-md-12'),
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
            Field('name', wrapper_class='col-md-12'),
            Field('start_time', wrapper_class='col-md-12'),
            Field('end_time', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = Expedient
        widgets = {
            'start_time': forms.TimeInput(format='%H:%m', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%m', attrs={'type': 'time'}),
        }
        fields = ['name', 'start_time', 'end_time']
