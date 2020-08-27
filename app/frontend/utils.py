#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 10:08.
from datetime import datetime

from service.models import OrderOfService
from frontend.icons import ICON_DASHBOARD


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
        'services': OrderOfService.objects.all()
    }
