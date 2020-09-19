#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/09/2020 13:47.
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class InvoiceForm(forms.ModelForm):
    prefix = "invoiceform"

    layout = Layout(
        Row(
            Field('type_of_payment'),
            Field('status'),
            PrependedText('value', 'R$'),
            Field('date'),
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
        model = Invoice
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_payment', 'status', 'value', 'date', 'observation', ]
