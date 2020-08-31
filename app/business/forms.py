#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/08/2020 09:22.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms
from django.forms import TextInput

from .models import *


class BusinessDayForm(forms.ModelForm):
    prefix = "businessdayform"

    start = forms.CharField()
    end = forms.CharField()

    layout = Layout(
        Row(
            # Field('day', wrapper_class='col-md'),
            Field('start', wrapper_class='col-md', type='hidden'),
            Field('end', wrapper_class='col-md', type='hidden'),
            Field('color', wrapper_class='col-md'),
            Field('expedient_day', wrapper_class='col-md'),
            Field('is_work_day', wrapper_class='col-md'),
            Field('force_day_full', wrapper_class='col-md'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.fields['start'].required = False
        # self.fields['start'].label = 'Data Início'
        self.fields['end'].required = False
        # self.fields['end'].label = 'Data Fim'

    class Meta:
        model = BusinessDay
        widgets = {
            # 'day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'color': TextInput(attrs={'type': 'color'}),
        }
        fields = ['color', 'expedient_day', 'is_work_day', 'force_day_full', 'start', 'end']


class ExpedientForm(forms.ModelForm):
    prefix = "expedientform"

    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md'),
            Field('start_time', wrapper_class='col-md'),
            Field('end_time', wrapper_class='col-md'),
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
        model = Expedient
        widgets = {
            'start_time': forms.DateInput(format='%H:%m', attrs={'type': 'time'}),
            'end_time': forms.DateInput(format='%H:%m', attrs={'type': 'time'}),
        }
        fields = ['name', 'start_time', 'end_time']
