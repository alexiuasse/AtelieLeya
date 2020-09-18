#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/09/2020 11:44.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class OrderOfServiceFormFrontend(forms.ModelForm):
    prefix = "orderOfServicefrontend"

    time = forms.ChoiceField(label="Horário")
    businessday = forms.IntegerField(required=False)

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-lg-12'),
            Field('date', wrapper_class='col-lg-12'),
            Field('time', wrapper_class='col-lg-12'),
            Field('observation', wrapper_class='col-lg-12'),
            Field('businessday', wrapper_class='col-lg-12', type='hidden'),
        ),
    )

    def __init__(self, *args, **kwargs):
        q_tp_s = kwargs.pop('query_tp_s') if 'query_tp_s' in kwargs else None
        times = kwargs.pop('times') if 'times' in kwargs else None
        businessday_pk = kwargs.pop('businessday_pk') if 'businessday_pk' in kwargs else None
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.fields['type_of_service'].queryset = q_tp_s
        self.fields['time'].choices = times
        self.fields['businessday'].initial = businessday_pk

    class Meta:
        model = OrderOfService
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'readonly': True}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'date', 'time', 'observation', 'businessday']


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
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'date', 'time',
                  'confirmed', 'observation', 'status', 'canceled']
