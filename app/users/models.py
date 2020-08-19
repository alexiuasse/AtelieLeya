#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/08/2020 09:56.

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateField('data de nascimento', blank=True, null=True)
    order_of_service = models.ManyToManyField("service.OrderOfService", verbose_name="Procedimentos", blank=True)

    def get_total_points(self):
        return sum(s.type_of_service.quantity_points for s in self.order_of_service)

    def get_total_used_points(self):
        return sum(s.type_of_service.quantity_points for s in self.order_of_service if s.counted)

    def get_total_unused_points(self):
        return sum(s.type_of_service.quantity_points for s in self.order_of_service if not s.counted)
