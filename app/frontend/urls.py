#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/09/2020 19:07.

from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home', HomePage.as_view(), name='homepage'),
    path('login/admin/', auth_views.LoginView.as_view(template_name='login.html'), name='login_admin'),
    path('login/frontend/', auth_views.LoginView.as_view(template_name='homepage/login.html'), name='login_frontend'),
    path('logout/admin/', LogoutAdmin.as_view(), name='logout_admin'),
    path('logout/frontend/', LogoutFrontend.as_view(), name='logout_frontend'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('chart/<int:year>/', Chart.as_view(), name='chart'),
]
