#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 13/09/2020 10:51.
from django.urls import path, include

from .views import *

app_name = 'worker'

workerprofile_patterns = ([
                              path('', WorkerProfileView.as_view(), name='view'),
                              path('<int:pk>/profile/', WorkerProfileProfile.as_view(), name='profile'),
                              path('create/', WorkerProfileCreate.as_view(), name='create'),
                              path('<int:pk>/edit/', WorkerProfileEdit.as_view(), name='edit'),
                              path('<int:pk>/delete/', WorkerProfileDel.as_view(), name='delete'),
                          ], 'workerprofile')

urlpatterns = [
    path('', include(workerprofile_patterns)),
]
