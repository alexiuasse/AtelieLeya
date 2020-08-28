#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/08/2020 18:14.
from django.urls import path, include

from .views import *

app_name = "business"

expedient_day_patterns = ([
                              path('create/', ExpedientCreate, name='create'),
                              path('<int:pk>/edit/', ExpedientEdit.as_view(), name='edit'),
                              path('<int:pk>/delete/', ExpedientDel.as_view(), name='delete'),
                          ], 'expedient')

business_day_patterns = ([
                             path('check/full/', check_if_day_is_full, name='check_full'),
                             path('create/', businessday_create, name='create'),
                             path('<int:pk>/profile/', BusinessDayProfile.as_view(), name='profile'),
                             path('<int:pk>/edit/', BusinessDayEdit.as_view(), name='edit'),
                             path('<int:pk>/delete/', BusinessDayDel.as_view(), name='delete'),
                         ], 'businessday')

urlpatterns = [
    path('businessday/', include(business_day_patterns)),
    path('expedient/', include(expedient_day_patterns)),
]
