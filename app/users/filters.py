#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/11/2020 09:53.
from django_filters import FilterSet

from .models import Profile, RewardRetrieved


class ProfileFilter(FilterSet):
    class Meta:
        model = Profile
        fields = {'name': ['icontains'], 'whatsapp': ['icontains']}


class RewardRetrievedFilter(FilterSet):
    class Meta:
        model = RewardRetrieved
        fields = {'customer__profile__name': ['icontains']}
