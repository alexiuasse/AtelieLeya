#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 14:52.

from django.contrib import admin

from .models import *

admin.site.register(Expedient)
admin.site.register(BusinessDay)
