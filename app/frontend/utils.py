#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 26/08/2020 08:51.
from datetime import datetime

from service.models import OrderOfService


def context_dashboard():
    return {
        'start_date': datetime.today().date,
        'title': 'Dashboard',
        'subtitle': 'Dashboard',
        'services': OrderOfService.objects.all()
    }
