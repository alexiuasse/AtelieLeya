#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 15/09/2020 20:55.
from django.urls import path, include

from .views import *

app_name = "service"

calendar_patterns = ([
                         path('admin', ServiceCalendarAdmin.as_view(), name='admin'),
                         path('customer', ServiceCalendarCustomer.as_view(), name='customer'),
                     ], 'calendar')

order_of_service_patterns = ([
                                 path('change/date/', OrderOfServiceChangeDate.as_view(), name='change_date'),
                                 path('<int:pk>/get/frontend/', OrderOfServiceGetFrontend.as_view(),
                                      name='get_frontend'),
                                 path('<int:day>/<int:month>/<int:year>/create/frontend/',
                                      OrderOfServiceCreateFrontend.as_view(), name='create_frontend'),
                                 path('<int:cpk>/create/', OrderOfServiceCreate.as_view(), name='create'),
                                 path('<int:cpk>/<int:pk>/profile/', OrderOfServiceProfile.as_view(), name='profile'),
                                 path('<int:cpk>/<int:pk>/edit/', OrderOfServiceEdit.as_view(), name='edit'),
                                 path('<int:cpk>/<int:pk>/delete/', OrderOfServiceDel.as_view(), name='delete'),
                                 path('<int:pk>/confirmed/<int:flag>/', OrderOfServiceConfirmed.as_view(),
                                      name='confirmed'),
                                 path('<int:pk>/finished/<int:flag>/', OrderOfServiceFinished.as_view(),
                                      name='finished'),
                             ], 'orderofservice')

frontend_patterns = ([
                         path('<int:pk>/get/', get_order_of_service, name='get'),
                     ], 'frontend')

urlpatterns = [
    path('', include(order_of_service_patterns)),
    path('frontend/', include(frontend_patterns)),
    path('calendar/', include(calendar_patterns)),
]
