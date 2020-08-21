#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 19:07.
from django_tables2 import TemplateColumn, tables, Column

from .models import CustomUser


class CustomUserTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')
    name = Column(accessor='first_name', verbose_name='Nome', linkify=True)

    class Meta:
        model = CustomUser
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['name', 'username', 'whatsapp', 'birth_day']
