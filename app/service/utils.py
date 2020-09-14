#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/09/2020 11:35.

def update_points(orderofservice):
    if orderofservice.finished and not orderofservice.counted:
        orderofservice.customer.profile.total_of_points += orderofservice.type_of_service.rewarded_points
        orderofservice.customer.profile.save()
        orderofservice.save(update_fields={'counted': True})
