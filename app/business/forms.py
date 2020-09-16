#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 14:27.
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
            # Field('day', wrapper_class='col-md-12'),
            Field('start', wrapper_class='col-md-12', type='hidden'),
            Field('end', wrapper_class='col-md-12', type='hidden'),
            Field('color', wrapper_class='col-md-12'),
            Field('expedient_day', wrapper_class='col-md-12'),
            Field('workers', wrapper_class='col-md-12'),
            Field('is_work_day', wrapper_class='col-md-12'),
            Field('force_day_full', wrapper_class='col-md-12'),
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
        fields = ['color', 'expedient_day', 'workers', 'is_work_day', 'force_day_full', 'start', 'end']
