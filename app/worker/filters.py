#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 09:42.
from django_filters import FilterSet

from .models import *


class WorkerProfileFilter(FilterSet):
    class Meta:
        model = WorkerProfile
        fields = {'name': ['icontains'], }
