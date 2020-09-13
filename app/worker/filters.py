#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 13/09/2020 10:59.
from django_filters import FilterSet

from .models import *


class WorkerProfileFilter(FilterSet):
    class Meta:
        model = WorkerProfile
        fields = {'customuser__first_name': ['icontains'], }
