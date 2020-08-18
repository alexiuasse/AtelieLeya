#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 14:53.
from django_filters import FilterSet

from .models import *


class RewardFilter(FilterSet):
    class Meta:
        model = StatusService
        fields = {'name': ['icontains'], }


class TypeOfServiceFilter(FilterSet):
    class Meta:
        model = TypeOfService
        fields = {'name': ['icontains'], }


class StatusServiceFilter(FilterSet):
    class Meta:
        model = StatusService
        fields = {'name': ['icontains'], }
