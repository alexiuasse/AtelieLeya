#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 10:24.
from django_filters import FilterSet

from .models import *


class InvoiceFilter(FilterSet):
    class Meta:
        model = Invoice
        fields = {'date', }
