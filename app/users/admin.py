#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/08/2020 10:21.

# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)
