#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 16:54.
from django_filters import FilterSet

from .models import CustomUser


class CustomUserFilter(FilterSet):
    class Meta:
        model = CustomUser
        fields = {'first_name', }
