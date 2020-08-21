#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 13:54.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class OrderOfServiceForm(forms.ModelForm):
    prefix = "orderOfService"

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-md'),
            Field('date', wrapper_class='col-md'),
            Field('time', wrapper_class='col-md'),
            Field('finished', wrapper_class='col-md'),
            Field('confirmed', wrapper_class='col-md'),
            # Field('counted', wrapper_class='col-md'),
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
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'date', 'time',
                  'finished', 'confirmed', 'observation']
