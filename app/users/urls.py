#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 18:39.

from django.urls import path, include

from .views import *

app_name = "users"

user_patterns = ([
                     path('', CustomUserView.as_view(), name='view'),
                     path('create/', CustomUserCreate.as_view(), name='create'),
                     path('<int:pk>/profile/', CustomUserProfile.as_view(), name='profile'),
                     path('<int:pk>/edit/', CustomUserEdit.as_view(), name='edit'),
                     path('<int:pk>/delete/', CustomUserDel.as_view(), name='delete'),
                 ], 'customuser')

urlpatterns = [
    path('/', include(user_patterns)),
    path('signup/', signup, name='signup'),
]
