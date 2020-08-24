#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 13:50.
#
# from .models import OrderOfService
#
#
# @receiver(post_save, sender=OrderOfService)
# def count_points(sender, instance, created, **kwargs):
#     """
#     If OrderOfService is finished and has not been counted yet, count it and set to counted
#     :param sender:
#     :param instance:
#     :param created:
#     :param kwargs:
#     :return:
#     """
#     if instance.finished and not instance.counted:
#         instance.customer.total_of_points += instance.type_of_service.rewarded_points
#         instance.customer.save()
#         instance.update(counted=True)
