#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/09/2020 12:32.

# users/admin.py
from django.contrib import admin

from .models import Profile, RewardRetrieved

admin.site.register(RewardRetrieved)
admin.site.register(Profile)
#
#
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     fieldsets = (
#         *UserAdmin.fieldsets,  # original form fieldsets, expanded
#         (  # new fieldset added on to the bottom
#             'Campos Personalizados',  # group heading of your choice; set to None for a blank space instead of a header
#             {
#                 'fields': (
#                     'whatsapp',
#                     'birth_day',
#                     'total_of_points',
#                     # 'total_of_points_redeemed',
#                     # 'total_of_points_not_redeemed',
#                 ),
#             },
#         ),
#     )
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
