#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 20/08/2020 10:01.
from django.urls import path

from .views import *

app_name = "service"

urlpatterns = [
    path('calendar/admin/', ServiceCalendarAdmin.as_view(), name='calendar-admin'),
    path('calendar/customer/', ServiceCalendarCustomer.as_view(), name='calendar-customer'),
    path('<int:status>/<int:day>/<int:month>/<int:year>/<int:scheduled>/', OrderOfServiceIndex.as_view(), name='index'),
    path('view/', OrderOfServiceView.as_view(), name='view'),
    path('<int:cpk>/<int:ctp>/<int:dev>/<int:pk>/profile/', OrderOfServiceProfile.as_view(), name='profile'),
    path('<int:cpk>/<int:ctp>/<int:dev>/create/', OrderOfServiceCreate.as_view(), name='create'),
    path('<int:cpk>/<int:ctp>/<int:dev>/<int:pk>/edit/', OrderOfServiceEdit.as_view(), name='edit'),
    path('<int:cpk>/<int:ctp>/<int:dev>/<int:pk>/delete/', OrderOfServiceDel.as_view(), name='delete'),
]
