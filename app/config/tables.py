#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/08/2020 10:02.
from django.utils.safestring import mark_safe
from django_tables2 import tables, TemplateColumn

from .models import *


class TypeOfPaymentTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = TypeOfPayment
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']


class RewardTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'quantity_in_points']


class TypeOfServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = TypeOfService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'value', 'time', 'rewarded_points']

    @staticmethod
    def render_value(value):
        return mark_safe(f"R$ {value}")

    @staticmethod
    def render_time(value):
        return mark_safe(f"{value} min")


class StatusServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual']

    @staticmethod
    def render_contextual(value):
        return mark_safe(f'<span class="badge bg-{ContextualEnum[value].value}">Status</span>')


class StatusPaymentTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusPayment
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual']

    @staticmethod
    def render_contextual(value):
        return mark_safe(f'<span class="badge bg-{ContextualEnum[value].value}">Status</span>')
