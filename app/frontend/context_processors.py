#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 14:27.

from django.conf import settings  # import the settings file
from .icons import *


def frontend_template_context(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'NAME_OF_ENTERPRISE': settings.NAME_OF_ENTERPRISE,
        'VERSION': settings.VERSION,
        'ICON_HOME': ICON_HOME,
        'ICON_LOGOUT': ICON_LOGOUT,
        'ICON_LINK': ICON_LINK,
        'ICON_EYE': ICON_EYE,
        'ICON_ARROW_BACK': ICON_ARROW_BACK,
        'ICON_DELETE': ICON_DELETE,
        'ICON_EDIT': ICON_EDIT,
        'ICON_ADD': ICON_ADD,
        'ICON_CALENDAR': ICON_CALENDAR,
        'ICON_DEVICE': ICON_DEVICE,
        'ICON_PERSON': ICON_PERSON,
        'ICON_NEW_PERSON': ICON_NEW_PERSON,
        'ICON_SETTINGS': ICON_SETTINGS,
        'ICON_TRIANGLE_ALERT': ICON_TRIANGLE_ALERT,
        'ICON_BUG': ICON_BUG,
        'ICON_SERVICE': ICON_SERVICE,
        'ICON_DASHBOARD': ICON_DASHBOARD,
    }
