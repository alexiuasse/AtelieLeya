#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 20/08/2020 14:50.
from django.urls import path, include

from .views import *

app_name = "service"

calendar_patterns = ([
                         path('admin', ServiceCalendarAdmin.as_view(), name='admin'),
                         path('customer', ServiceCalendarCustomer.as_view(), name='customer'),
                     ], 'calendar')

urlpatterns = [
    path('calendar/', include(calendar_patterns)),
    path('<int:status>/<int:day>/<int:month>/<int:year>/<int:scheduled>/', OrderOfServiceIndex.as_view(), name='index'),
    path('view/', OrderOfServiceView.as_view(), name='view'),
    path('<int:cpk>/<int:ctp>/<int:dev>/<int:pk>/profile/', OrderOfServiceProfile.as_view(), name='profile'),
    path('<int:cpk>/<int:ctp>/<int:dev>/create/', OrderOfServiceCreate.as_view(), name='create'),
    path('<int:cpk>/<int:ctp>/<int:dev>/<int:pk>/edit/', OrderOfServiceEdit.as_view(), name='edit'),
    path('<int:cpk>/<int:ctp>/<int:dev>/<int:pk>/delete/', OrderOfServiceDel.as_view(), name='delete'),
]
