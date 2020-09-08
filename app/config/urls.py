#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/09/2020 14:00.

from django.urls import path, include

from .views import *

app_name = "config"

type_of_payment_patterns = ([
                                path('', TypeOfPaymentView.as_view(), name='view'),
                                path('create/', TypeOfPaymentCreate.as_view(), name='create'),
                                path('<int:pk>/edit/', TypeOfPaymentEdit.as_view(), name='edit'),
                                path('<int:pk>/del', TypeOfPaymentDel.as_view(), name='delete'),
                            ], 'typeofpayment')

reward_patterns = ([
                       path('', RewardView.as_view(), name='view'),
                       path('create/', RewardCreate.as_view(), name='create'),
                       path('<int:pk>/edit/', RewardEdit.as_view(), name='edit'),
                       path('<int:pk>/del', RewardDel.as_view(), name='delete'),
                   ], 'reward')

type_of_service_patterns = ([
                                path('', TypeOfServiceView.as_view(), name='view'),
                                path('<int:pk>/get/value/', TyperOfServiceGetValue.as_view(), name='value'),
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

status_payment_patterns = ([
                               path('', StatusPaymentView.as_view(), name='view'),
                               path('create/', StatusPaymentCreate.as_view(), name='create'),
                               path('<int:pk>/edit/', StatusPaymentEdit.as_view(), name='edit'),
                               path('<int:pk>/del', StatusPaymentDel.as_view(), name='delete'),
                           ], 'statuspayment')

expedient_day_patterns = ([
                              path('', ExpedientView.as_view(), name='view'),
                              path('create/', ExpedientCreate.as_view(), name='create'),
                              path('<int:pk>/edit/', ExpedientEdit.as_view(), name='edit'),
                              path('<int:pk>/delete/', ExpedientDel.as_view(), name='delete'),
                          ], 'expedient')

urlpatterns = [
    path('', Config.as_view(), name='index'),
    path('typeofpayment/', include(type_of_payment_patterns)),
    path('reward/', include(reward_patterns)),
    path('typeofservice/', include(type_of_service_patterns)),
    path('statusservice/', include(status_service_patterns)),
    path('statuspayment/', include(status_payment_patterns)),
    path('expedient/', include(expedient_day_patterns)),
]
