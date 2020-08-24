#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 10:24.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class InvoiceForm(forms.ModelForm):
    prefix = "invoiceform"

    layout = Layout(
        Row(
            # Field('order_of_service', wrapper_class='col-md'),
            Field('type_of_payment', wrapper_class='col-md'),
            Field('value', wrapper_class='col-md'),
            Field('date', wrapper_class='col-md'),
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
        model = Invoice
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_payment', 'value', 'date', 'observation', ]
