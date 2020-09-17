#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/09/2020 18:45.
from django.urls import path, include

from .views import *

app_name = "business"

business_day_patterns = ([
                             path('create/', businessday_create, name='create'),
                             path('<int:pk>/profile/', business_profile, name='profile'),
                             path('<int:pk>/edit/', BusinessDayEdit.as_view(), name='edit'),
                             path('<int:pk>/delete/', BusinessDayDel.as_view(), name='delete'),
                         ], 'businessday')

admin_patterns = ([
                      path('calendar/', business_calendar, name='calendar'),
                      path('calendar/data/', get_calendar_data_admin, name='data'),
                  ], 'admin')

frontend_patterns = ([
                         path('calendar/data/', get_calendar_data_frontend, name='data'),
                     ], 'frontend')

utils_patterns = ([
                      path('<int:bpk>/<int:pk>/get/hours/', businessday_get_hours, name='hours'),
                      path('<int:d>/<int:m>/<int:y>/check/', check_businessday, name='check')
                  ], 'utils')

urlpatterns = [
    path('businessday/', include(business_day_patterns)),
    path('admin/', include(admin_patterns)),
    path('frontend/', include(frontend_patterns)),
    path('utils/', include(utils_patterns)),
]
