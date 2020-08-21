#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 14:48.
from django.urls import path, include

from .views import *

app_name = "service"

calendar_patterns = ([
                         path('admin', ServiceCalendarAdmin.as_view(), name='admin'),
                         path('customer', ServiceCalendarCustomer.as_view(), name='customer'),
                     ], 'calendar')

order_of_service_patterns = ([
                                 path('<int:cpk>/create/', OrderOfServiceCreate.as_view(), name='create'),
                                 path('<int:cpk>/<int:pk>/profile/', OrderOfServiceProfile.as_view(), name='profile'),
                                 path('<int:cpk>/<int:pk>/edit/', OrderOfServiceEdit.as_view(), name='edit'),
                                 path('<int:cpk>/<int:pk>/delete/', OrderOfServiceDel.as_view(), name='delete'),
                                 path('<int:cpk>/<int:pk>/confirmed/', confirmed_service, name='confirmed'),
                                 path('<int:cpk>/<int:pk>/finished/', finished_service, name='finished'),
                             ], 'orderofservice')

urlpatterns = [
    path('', include(order_of_service_patterns)),
    path('calendar/', include(calendar_patterns)),
]
