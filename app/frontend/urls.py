#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/09/2020 11:43.

from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_user, name='logout'),
    path('home/', homepage, name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('maintenance/', maintenance, name='maintenance'),
    path('chart/<int:year>/', chart, name='chart'),
]
