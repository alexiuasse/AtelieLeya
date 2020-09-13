#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 13/09/2020 12:44.
from django_tables2 import tables, TemplateColumn, Column

from .models import *


class WorkerProfileTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')
    username = Column(linkify=True, accessor='get_username', verbose_name="Usuário")

    class Meta:
        model = WorkerProfile
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['username', ]
