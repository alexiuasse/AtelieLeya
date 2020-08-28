#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/08/2020 12:31.
from datetime import datetime

from business.models import BusinessDay
from django.http import JsonResponse
from frontend.icons import ICON_DASHBOARD
from service.models import OrderOfService


def get_calendar_data_admin(request):
    start = datetime.strptime(request.GET.get('start', None), "%Y-%m-%dT%H:%M:%SZ")
    end = datetime.strptime(request.GET.get('end', None), "%Y-%m-%dT%H:%M:%SZ")
    orderofservices = OrderOfService.objects.filter(date__range=[start, end])
    data = []
    for s in orderofservices:
        data.append({
            'pk': s.pk,
            'title': s.get_name_html(),
            'start': f"{s.date}T{s.time}",
            'url': s.get_absolute_url(),
            'color': s.type_of_service.contextual,
        })
    businessday = BusinessDay.objects.filter(day__range=[start, end])
    for b in businessday:
        data.append({
            'pk': b.pk,
            'title': b.get_name_html(),
            'start': b.get_start_date_time(),
            'end': b.get_end_date_time(),
            'color': b.color,
        })
    return JsonResponse({'data': data})


def context_dashboard():
    return {
        'config': {
            'title': {
                'text': 'Dashboard',
                'icon': ICON_DASHBOARD
            },
            'pre_title': 'Dashboard',
        },
        'start_date': datetime.today().date,
    }
