#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 16:09.

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


# REMEMBER: ALWAYS set the fields or the form will not save correctly.


class BaseConfigForm(forms.ModelForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.helper.label_class = 'bmd-label-floating'


class RewardForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('quantity_in_points', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = Reward
        fields = ['name', 'quantity_in_points']


class TypeOfServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('rewarded_points', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = TypeOfService
        fields = ['name', 'rewarded_points']


class StatusServiceForm(BaseConfigForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('contextual', wrapper_class='col-md-12'),
        ),
    )

    class Meta:
        model = StatusService
        fields = ['name', 'contextual']
