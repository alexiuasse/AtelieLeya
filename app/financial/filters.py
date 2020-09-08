#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/09/2020 14:24.
from django_filters import FilterSet

from .models import *


class InvoiceFilter(FilterSet):
    class Meta:
        model = Invoice
        fields = {'date': ['icontains'], }
