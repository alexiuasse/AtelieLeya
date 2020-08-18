#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 14:57.

from django.urls import path, include

from .views import *

app_name = "config"

reward_patterns = ([
                       path('', RewardView.as_view(), name='view'),
                       path('create/', RewardCreate.as_view(), name='create'),
                       path('<int:pk>/edit/', RewardEdit.as_view(), name='edit'),
                       path('<int:pk>/del', RewardDel.as_view(), name='delete'),
                   ], 'reward')

type_of_service_patterns = ([
                                path('', TypeOfServiceView.as_view(), name='view'),
                                path('create/', TypeOfServiceCreate.as_view(), name='create'),
                                path('<int:pk>/edit/', TypeOfServiceEdit.as_view(), name='edit'),
                                path('<int:pk>/del', TypeOfServiceDel.as_view(), name='delete'),
                            ], 'typeofservice')

status_service_patterns = ([
                               path('', StatusServiceView.as_view(), name='view'),
                               path('create/', StatusServiceCreate.as_view(), name='create'),
                               path('<int:pk>/edit/', StatusServiceEdit.as_view(), name='edit'),
                               path('<int:pk>/del', StatusServiceDel.as_view(), name='delete'),
                           ], 'statusservice')

urlpatterns = [
    path('', Config.as_view(), name='index'),
    path('reward/', include(reward_patterns)),
    path('typeofservice/', include(type_of_service_patterns)),
    path('statusservice/', include(status_service_patterns)),
]
