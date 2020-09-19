#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/09/2020 15:16.
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class OrderOfServiceFormFrontend(forms.ModelForm):
    prefix = "orderOfServicefrontend"

    time = forms.ChoiceField(label="Horário")
    value = forms.FloatField(label="Valor")
    businessday = forms.IntegerField(required=False)

    layout = Layout(
        Row(
            Field('type_of_service'),
            PrependedText('value', 'R$'),
            Field('date'),
            Field('time'),
            Field('observation'),
            Field('businessday', type='hidden'),
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
        self.fields['value'].widget.attrs['readonly'] = True

    class Meta:
        model = OrderOfService
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'readonly': True}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'value', 'date', 'time', 'observation', 'businessday']


class OrderOfServiceForm(forms.ModelForm):
    prefix = "orderOfService"

    layout = Layout(
        Row(
            Field('type_of_service'),
            Field('date'),
            Field('time'),
            Field('confirmed'),
            Field('canceled'),
            Field('status'),
            Field('observation'),
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
