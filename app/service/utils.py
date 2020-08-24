#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 13:49.

def update_points(orderofservice):
    if orderofservice.finished and not orderofservice.counted:
        orderofservice.customer.total_of_points += orderofservice.type_of_service.rewarded_points
        orderofservice.customer.save()
        orderofservice.save(update_fields={'counted': True})
