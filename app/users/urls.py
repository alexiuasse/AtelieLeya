#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/09/2020 18:44.

from django.urls import path, include

from .views import *

app_name = "users"

user_patterns = ([
                     path('', CustomUserView.as_view(), name='view'),
                     path('create/', CustomUserCreate.as_view(), name='create'),
                     path('<int:pk>/profile/admin/', CustomUserProfileAdmin.as_view(), name='profile_admin'),
                     path('profile/frontend/', CustomUserProfileFrontend.as_view(), name='profile_frontend'),
                     path('<int:pk>/edit/', CustomUserEdit.as_view(), name='edit'),
                     path('edit/frontend/', CustomUserEditFrontend.as_view(), name='edit_frontend'),
                     path('<int:pk>/delete/', CustomUserDel.as_view(), name='delete'),
                 ], 'customuser')

urlpatterns = [
    path('', include(user_patterns)),
    path('signup/admin/', signup, name='signup'),
    path('signup/frontend/', signup_frontend, name='signup_frontend'),
]
