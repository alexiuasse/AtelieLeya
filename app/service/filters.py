#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/09/2020 14:24.
from django_filters import FilterSet

from .models import *


class OrderOfServiceFilter(FilterSet):
    class Meta:
        model = OrderOfService
        fields = {'type_of_service__name': ['icontains'], }
