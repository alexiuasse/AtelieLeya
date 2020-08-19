#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/08/2020 09:47.

from django.contrib import admin
from .models import *

admin.site.register(Reward)
admin.site.register(TypeOfService)
admin.site.register(StatusService)
