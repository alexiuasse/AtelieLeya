#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/08/2020 12:31.

from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import *
from .utils import get_calendar_data_admin

app_name = 'frontend'

calendar_data_patterns = ([
                              path('data/', get_calendar_data_admin, name='data'),
                          ], 'calendar')

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home', HomePage.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('calendar/', include(calendar_data_patterns)),
]
