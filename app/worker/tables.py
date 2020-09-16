#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 09:42.
from django_tables2 import tables, TemplateColumn, Column

from .models import *


class WorkerProfileTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')
    name = Column(linkify=True)

    class Meta:
        model = WorkerProfile
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['name', 'expertise', 'user']
