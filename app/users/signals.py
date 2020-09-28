#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/09/2020 07:44.
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(user_signed_up)
def populate_profile(sociallogin, user, **kwargs):
    # if sociallogin.account.provider == 'facebook':
    #     user_data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
    #     picture_url = "http://graph.facebook.com/" + sociallogin.account.uid + "/picture?type=large"
    #     full_name = user_data['name']

    if sociallogin.account.provider == 'google':
        user_data = user.socialaccount_set.filter(provider='google')[0].extra_data
        picture_url = user_data['picture']
        full_name = user_data['name']

        user.profile.picture = picture_url
        user.profile.name = full_name
        user.profile.save()
