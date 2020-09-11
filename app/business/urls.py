#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 11/09/2020 16:16.
from django.urls import path, include

from .views import *
from .mcalendar import *

app_name = "business"

business_day_patterns = ([
                             # path('check/full/', check_if_day_is_full, name='check_full'),
                             path('create/', businessday_create, name='create'),
                             path('<int:pk>/profile/', BusinessDayProfile.as_view(), name='profile'),
                             path('<int:pk>/edit/', BusinessDayEdit.as_view(), name='edit'),
                             path('<int:pk>/delete/', BusinessDayDel.as_view(), name='delete'),
                         ], 'businessday')

my_calendar_patterns = ([
                            path('data/admin/', get_calendar_data_admin, name='data_admin'),
                            path('data/frontend/<int:customer>/', get_calendar_data_frontend, name='data_frontend'),
                            path('view/', BusinessCalendarView.as_view(), name='view'),
                        ], 'calendar')

utils_patterns = ([
                      path('<int:bpk>/<int:pk>/get/hours/', businessday_get_hours, name='hours')
                  ], 'utils')

urlpatterns = [
    path('businessday/', include(business_day_patterns)),
    path('calendar/', include(my_calendar_patterns)),
    path('utils/', include(utils_patterns)),
]
