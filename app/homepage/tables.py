#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 10:46.

# from django.utils.safestring import mark_safe
# from django_tables2 import tables, TemplateColumn, Column
#
# from .models import *


# class TestimonialsTable(tables.Table):
#     title = Column(linkify=lambda record: record.get_edit_url())
#     _ = TemplateColumn(template_name='base/table/buttons.html')
#
#     class Meta:
#         model = Testimonials
#         attrs = {'class': 'table table-striped table-hover'}
#         per_page = 10
#         fields = ['title', 'subtitle', 'testimonial', 'image', 'show']
#
#
# class ClientsImageTable(tables.Table):
#     name = Column(linkify=lambda record: record.get_edit_url())
#     _ = TemplateColumn(template_name='base/table/buttons.html')
#
#     class Meta:
#         model = ClientsImage
#         attrs = {'class': 'table table-striped table-hover'}
#         per_page = 10
#         fields = ['name', 'image', 'show']
