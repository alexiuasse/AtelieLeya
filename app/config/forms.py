#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 17:18.
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
        ),
    )

    class Meta:
        model = Reward
        fields = ['name', 'quantity_in_points']


class TypeOfServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('contextutal', wrapper_class='col-md-12'),
            PrependedText('value', 'R$', wrapper_class='col-md-12'),
            AppendedText('time', 'min', wrapper_class='col-md-12'),
            Field('rewarded_points', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = TypeOfService
        widgets = {
            'contextutal': TextInput(attrs={'type': 'color'}),
        }
        fields = ['name', 'contextutal', 'value', 'time', 'rewarded_points']


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
