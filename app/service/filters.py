#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/08/2020 10:06.
from django_filters import FilterSet

from .models import *


class OrderOfServiceFilter(FilterSet):
    class Meta:
        model = OrderOfService
        fields = {'type_of_service', }
