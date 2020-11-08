#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 10:48.

from django.contrib import admin
from .models import *

admin.site.register(Reward)
admin.site.register(TypeOfService)
admin.site.register(TypeOfPayment)
admin.site.register(StatusService)
admin.site.register(StatusPayment)
admin.site.register(Expedient)
# admin.site.register(HomePage)
