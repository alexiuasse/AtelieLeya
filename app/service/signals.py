#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/09/2020 11:29.
#
from config.models import StatusPayment
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from financial.models import Invoice

from .models import OrderOfService


@receiver(post_save, sender=OrderOfService)
def count_points(sender, instance, created, **kwargs):
    if instance.finished and not instance.counted:
        instance.customer.profile.total_of_points += instance.type_of_service.rewarded_points
        instance.customer.profile.save()
        OrderOfService.objects.filter(pk=instance.pk).update(counted=True)

    # if instance is created, then create a new invoice
    if created:
        Invoice(
            order_of_service=instance,
            type_of_payment=None,
            status=get_object_or_404(StatusPayment, pk=settings.STATUS_PAYMENT_DEFAULT),
            value=instance.type_of_service.value,
        ).save()

    if not created:
        OrderOfService.objects.filter(pk=instance.pk).update(
            finished=not instance.status.pk != settings.STATUS_SERVICE_FINISHED)
