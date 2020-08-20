#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 20/08/2020 11:19.

from django.urls import path

from .views import signup

app_name = "users"

urlpatterns = [
    path('signup/', signup, name='signup'),
]
