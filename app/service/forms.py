#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 07/09/2020 16:35.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class OrderOfServiceFormFrontend(forms.ModelForm):
    prefix = "orderOfServicefrontend"

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-lg-12'),
            Field('date', wrapper_class='col-lg-12'),
            Field('time', wrapper_class='col-lg-12'),
            Field('observation', wrapper_class='col-lg-12'),
        ),
    )

    def __init__(self, *args, **kwargs):
        q_tp_s = kwargs.pop('query_tp_s')
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.fields['type_of_service'].queryset = q_tp_s

    class Meta:
        model = OrderOfService
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'readonly': True}),
            'time': forms.TimeInput(format='%H:%m', attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'date', 'time', 'observation']


class OrderOfServiceForm(forms.ModelForm):
    prefix = "orderOfService"

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-md'),
            Field('date', wrapper_class='col-md'),
            Field('time', wrapper_class='col-md'),
            # Field('finished', wrapper_class='col-md'),
            Field('confirmed', wrapper_class='col-md'),
            Field('canceled', wrapper_class='col-md'),
            Field('status', wrapper_class='col-md'),
            Field('observation', wrapper_class='col-md'),
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
        model = OrderOfService
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'time': forms.TimeInput(format='%H:%m', attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'date', 'time',
                  'confirmed', 'observation', 'status', 'canceled']


class OrderOfServiceFullForm(forms.ModelForm):
    prefix = "orderOfServicefullform"

    layout = Layout(
        Row(
            Field('customer', wrapper_class='col-md'),
            Field('type_of_service', wrapper_class='col-md'),
            Field('date', wrapper_class='col-md'),
            Field('time', wrapper_class='col-md'),
            # Field('finished', wrapper_class='col-md'),
            Field('confirmed', wrapper_class='col-md'),
            Field('canceled', wrapper_class='col-md'),
            Field('status', wrapper_class='col-md'),
            Field('observation', wrapper_class='col-md'),
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
        model = OrderOfService
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['customer', 'type_of_service', 'date', 'time',
                  'confirmed', 'observation', 'status', 'canceled']
