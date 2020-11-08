#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 10:43.

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


# class ClientsImageForm(forms.ModelForm):
#     layout = Layout(
#         Row(
#             Field('name'),
#             Field('image'),
#             Field('show'),
#         ),
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.disable_csrf = True
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = self.layout
#         self.helper.form_class = 'form-control'
#
#     class Meta:
#         model = ClientsImage
#         fields = ['name', 'image', 'show']
#
#
# class TestimonialsForm(forms.ModelForm):
#     layout = Layout(
#         Row(
#             Field('title'),
#             Field('subtitle'),
#             Field('testimonial'),
#             Field('image'),
#             Field('show'),
#         ),
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.disable_csrf = True
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = self.layout
#         self.helper.form_class = 'form-control'
#
#     class Meta:
#         model = Testimonials
#         widgets = {
#             'testimonial': forms.Textarea(attrs={"rows": 4}),
#         }
#         fields = ['title', 'subtitle', 'testimonial', 'image', 'show']


class HomePageForm(forms.ModelForm):
    layout = Layout(
        Row(
            Field('title'),
            Field('subtitle'),
            Field('address'),
            Field('whatsapp'),
            Field('whatsapp_link'),
            Field('instagram'),
            Field('facebook'),
            Field('first_image'),
            Field('first_video_url'),
            Field('second_image'),
            Field('second_video_url'),
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
        model = HomePage
        fields = ['title', 'subtitle', 'address', 'instagram', 'whatsapp', 'whatsapp_link', 'facebook', 'first_image',
                  'second_image', 'first_video_url', 'second_video_url']
