#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 10:58.

from django.urls import path, include

from .views import *

app_name = "users"

reward_retrieved_patterns = ([
                                 path('list/', RewardRetrievedList.as_view(), name='list'),
                                 path('<int:pk>/confirm/', reward_retrieved_confirm, name='confirm'),
                                 path('<int:cpk>/create/', RewardRetrievedCreate.as_view(), name='create'),
                                 path('<int:cpk>/<int:pk>/edit/', RewardRetrievedEdit.as_view(), name='edit'),
                                 path('<int:cpk>/<int:pk>/delete/', RewardRetrievedDelete.as_view(), name='delete'),
                             ], 'rewardretrieved')

admin_patterns = ([
                      path('signup/', signup, name='signup'),
                      path('view/', ProfileView.as_view(), name='view'),
                      path('<int:pk>/edit/', ProfileEdit.as_view(), name='edit'),
                      path('<int:pk>/delete/', ProfileDelete.as_view(), name='delete'),
                      path('<int:pk>/profile/', profile_admin, name='profile'),
                  ], 'admin')

frontend_patterns = ([
                         path('signup/', signup, name='signup'),
                         path('profile/', profile_frontend, name='profile'),
                         path('profile/update/', profile_update, name='update'),
                         path('reward/', reward_frontend, name='reward'),
                         path('calendar/', calendar_service_frontend, name='calendar'),
                         path('<int:rpk>/reward/retrieve/', reward_retrieve_frontend, name='reward_retrieve'),
                     ], 'frontend')

urlpatterns = [
    path('frontend/', include(frontend_patterns)),
    path('admin/', include(admin_patterns)),
    path('reward/', include(reward_retrieved_patterns)),
]
