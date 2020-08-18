#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 16:09.
from django_tables2 import tables, TemplateColumn

from .models import *


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
        fields = ['name', 'rewarded_points']


class StatusServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual']
