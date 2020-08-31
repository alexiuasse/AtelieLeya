#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/08/2020 13:33.
from datetime import datetime

from business.forms import BusinessDayForm
from frontend.icons import ICON_DASHBOARD


# def get_calendar_data_admin(request):
#     start = datetime.strptime(request.GET.get('start', None), "%Y-%m-%dT%H:%M:%SZ")
#     end = datetime.strptime(request.GET.get('end', None), "%Y-%m-%dT%H:%M:%SZ")
#     orderofservices = OrderOfService.objects.filter(date__range=[start, end])
#     data = []
#     for s in orderofservices:
#         data.append({
#             'type': 0,
#             'pk': s.pk,
#             'title': s.get_name_html(),
#             'start': f"{s.date}T{s.time}",
#             'url': s.get_absolute_url(),
#             'color': s.type_of_service.contextual,
#             'display': 'block',
#             'className': 'check' if s.get_contextual() else '',
#         })
#     businessday = BusinessDay.objects.filter(day__range=[start, end])
#     for b in businessday:
#         if b.is_work_day:
#             data.append({
#                 'type': 1,
#                 'pk': b.pk,
#                 'title': b.get_name_html(),
#                 'start': b.get_start_date_time(),
#                 'end': b.get_end_date_time(),
#                 'url': b.get_absolute_url(),
#                 'color': b.color,
#                 'display': 'block',
#             })
#         if b.get_is_full():
#             className = 'dayfull'
#         elif b.force_day_full:
#             className = 'forcedayfull'
#         elif not b.is_work_day:
#             className = 'notworkday'
#         else:
#             className = 'daynotfull'
#         data.append({
#             'isFull': 'true',
#             'start': b.get_start_date_time(),
#             'end': b.get_end_date_time(),
#             'allDay': 'true',
#             'display': 'background',
#             'className': className,
#         })
#     return JsonResponse({'data': data})


def context_dashboard():
    return {
        'config': {
            'title': {
                'text': 'Dashboard',
                'icon': ICON_DASHBOARD
            },
            'pre_title': 'Dashboard',
        },
    }
