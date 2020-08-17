#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/08/2020 15:32.

from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home', HomePage.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
