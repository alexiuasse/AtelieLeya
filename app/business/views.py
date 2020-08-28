#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 18:04.
from django.http import JsonResponse
from django.shortcuts import render
from .models import BusinessDay


def check_if_day_is_full(request):
    return JsonResponse({
        'is_full': BusinessDay.objects.get(day=request.GET.get('date', None)).get_is_full(),
    })
