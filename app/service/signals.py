#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 18:08.
#
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OrderOfService


@receiver(post_save, sender=OrderOfService)
def count_points(sender, instance, created, **kwargs):
    if instance.finished and not instance.counted:
        instance.customer.total_of_points += instance.type_of_service.rewarded_points
        instance.customer.save()
        OrderOfService.objects.filter(pk=instance.pk).update(counted=True)
