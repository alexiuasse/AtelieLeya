#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 09:06.
from django_tables2 import tables, TemplateColumn

from .models import *


class InvoiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Invoice
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['type_of_payment', 'value', 'date']
