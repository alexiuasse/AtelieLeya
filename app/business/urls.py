#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 17:43.
from django.urls import path, include

from .views import *

app_name = "business"

business_day_patterns = ([
                             path('check/full/', check_if_day_is_full, name='check_full'),
                         ], 'business')

urlpatterns = [
    path('', include(business_day_patterns)),
]
