#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 13/09/2020 12:47.
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


class WorkerProfileForm(forms.ModelForm):
    prefix = "workerprofile"

    layout = Layout(
        Row(
            Field('expertise', wrapper_class='col-md'),
            Field('customuser', wrapper_class='col-md'),
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
        model = WorkerProfile
        fields = ['expertise', 'customuser', ]
