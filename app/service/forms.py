#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/08/2020 10:09.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class OrderOfServiceForm(forms.ModelForm):
    prefix = "orderOfService"

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-md'),
            Field('date_time', wrapper_class='col-md'),
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
        # widgets = {
        #     'date_time': forms.DateTimeInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        #     'defect': forms.Textarea(attrs={"rows": 4}),
        #     'observation': forms.Textarea(attrs={"rows": 4}),
        # }
        fields = ['type_of_service', 'date_time']
