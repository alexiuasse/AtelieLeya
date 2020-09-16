#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 15/09/2020 23:01.
from django.urls import path, include

from .views import *

app_name = "service"

order_of_service_patterns = ([
                                 path('<int:cpk>/create/', OrderOfServiceCreate.as_view(), name='create'),
                                 path('<int:cpk>/<int:pk>/profile/', profile_order_of_service, name='profile'),
                                 path('<int:cpk>/<int:pk>/edit/', OrderOfServiceEdit.as_view(), name='edit'),
                                 path('<int:cpk>/<int:pk>/delete/', OrderOfServiceDel.as_view(), name='delete'),
                             ], 'orderofservice')

# utils admin
admin_patterns = ([
                      path('change/date/', change_date_order_of_service, name='change_date'),
                      path('<int:pk>/<int:flag>/confirm/', confirm_order_of_service, name='confirm'),
                      path('<int:pk>/<int:flag>/finish/', finish_order_of_service, name='finish'),
                  ], 'admin')

frontend_patterns = ([
                         path('<int:pk>/get/', get_order_of_service, name='get'),
                         path('<int:d>/<int:m>/<int:y>/create/', create_order_of_service, name='create'),
                     ], 'frontend')

urlpatterns = [
    path('', include(order_of_service_patterns)),
    path('admin/', include(admin_patterns)),
    path('frontend/', include(frontend_patterns)),
]
