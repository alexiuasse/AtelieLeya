#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/08/2020 18:00.
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms
from django.forms import TextInput, HiddenInput

from .models import *


class BusinessDayForm(forms.ModelForm):
    prefix = "businessdayform"

    start = forms.CharField()
    end = forms.CharField()

    layout = Layout(
        Row(
            Field('day', wrapper_class='col-md'),
            Field('color', wrapper_class='col-md'),
            Field('expedient_day', wrapper_class='col-md'),
            Field('is_work_day', wrapper_class='col-md'),
            Field('force_day_full', wrapper_class='col-md'),
            Field('start', wrapper_class='col-md', type="hidden"),
            Field('end', wrapper_class='col-md', type="hidden"),
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
        self.fields['end'].required = False

    class Meta:
        model = BusinessDay
        widgets = {
            'day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'color': TextInput(attrs={'type': 'color'}),
        }
        fields = ['day', 'color', 'expedient_day', 'is_work_day', 'force_day_full', 'start', 'end']


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
