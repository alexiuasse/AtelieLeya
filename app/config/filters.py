#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 10:47.
from django_filters import FilterSet

from .models import *


class TypeOfPaymentFilter(FilterSet):
    class Meta:
        model = TypeOfPayment
        fields = {'name': ['icontains'], }


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
