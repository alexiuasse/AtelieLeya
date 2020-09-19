#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/09/2020 13:47.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class WorkerProfileForm(forms.ModelForm):
    prefix = "workerprofile"

    layout = Layout(
        Row(
            Field('name'),
            Field('birth_date'),
            Field('whatsapp'),
            Field('expertise'),
            Field('user'),
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
