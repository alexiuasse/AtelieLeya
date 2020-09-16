#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 09:51.
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class WorkerProfileForm(forms.ModelForm):
    prefix = "workerprofile"

    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('birth_date', wrapper_class='col-md-12'),
            Field('whatsapp', wrapper_class='col-md-12'),
            Field('expertise', wrapper_class='col-md-12'),
            Field('user', wrapper_class='col-md-12'),
        ),
    )

    def __init__(self, *args, **kwargs):
        users = kwargs.pop('users') if 'users' in kwargs else None
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.fields['user'].queryset = users

    class Meta:
        model = WorkerProfile
        widgets = {
            'birth_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ['name', 'birth_date', 'whatsapp', 'expertise', 'user', ]
