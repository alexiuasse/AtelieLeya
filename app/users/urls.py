#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:13.

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

reward_retrieved_patterns = ([
                                 path('frontend/', RewardRetrieveFrontend.as_view(), name='retrieve_frontend'),
                                 path('<int:rpk>/frontend/create/', rewardretrieved_create,
                                      name='retrieve_frontend_create'),
                                 path('<int:cpk>/create/', RewardRetrievedCreate.as_view(), name='create'),
                                 path('<int:cpk>/<int:pk>/edit/', RewardRetrievedEdit.as_view(), name='edit'),
                                 path('<int:cpk>/<int:pk>/delete/', RewardRetrievedDel.as_view(), name='delete'),
                             ], 'rewardretrieved')

urlpatterns = [
    path('', include(user_patterns)),
    path('signup/admin/', signup, name='signup'),
    path('signup/frontend/', signup_frontend, name='signup_frontend'),
    path('reward/retrieved/', include(reward_retrieved_patterns)),
]
