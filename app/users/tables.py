#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 16:54.
from django_tables2 import TemplateColumn, tables

from .models import CustomUser


class CustomUserTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = CustomUser
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['first_name', 'last_name']
