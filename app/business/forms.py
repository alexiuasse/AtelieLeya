#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/09/2020 13:45.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, Column
from django import forms
from django.forms import TextInput

from .models import *


class BusinessDayForm(forms.ModelForm):
    prefix = "businessdayform"

    start = forms.CharField()
    end = forms.CharField()

    layout = Layout(
        Row(
            Field('start', type='hidden'),
            Field('end', type='hidden'),
            Field('color'),
            Field('expedient_day'),
            Field('workers'),
            Field('is_work_day'),
            Field('force_day_full'),
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


class CalendarFiltersForm(forms.Form):
    prefix = "calendarfilters"

    all = forms.BooleanField(initial=True)
    canceled = forms.BooleanField(initial=False)
    finished = forms.BooleanField(initial=False)
    confirmed = forms.BooleanField(initial=False)

    layout = Layout(
        Row(
            Column('all'),
            Column('canceled'),
            Column('finished'),
            Column('confirmed'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
