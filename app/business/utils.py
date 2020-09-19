#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/09/2020 09:51.

from .models import *


def datetime_range(start, end, delta):
    """
    Creating an range of time given an delta
    :param start: the start time
    :param end: the end time
    :param delta: the step value, ex.: 30
    :return: a list of range time
    """
    current = start
    while current < end:
        yield current
        current += delta


def check_if_has_other_service(date_time, businessday, order_of_service):
    """
    Verify if exists a orderofservice on the new date_time and if is not the same order_of_service
    :param date_time:
    :param businessday:
    :param order_of_service:
    :return:
    """
    # if the date_time is not in the remain hours of the day
    if date_time not in businessday.get_remain_hours_list():
        start = datetime.datetime.combine(order_of_service.date, order_of_service.time)
        # the estimate end of service
        end = (start + datetime.timedelta(minutes=order_of_service.type_of_service.time))
        time_occupied = datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME))
        if date_time in time_occupied:
            return True
        return False
    return True


def check_if_service_fits(businessday, order_of_service):
    """
    Check if order_of_service fit in the businessday
    :param businessday:
    :param order_of_service:
    :return: True if fits and False if not
    """
    slices = order_of_service.type_of_service.time / settings.SLICE_OF_TIME  # how many slices is need for this service
    response = businessday.get_tuple_remain_hours()
    # only check if it needs more than one slice of time, because if it needs so must be sequentially
    if slices > 1:
        # for each available hours, check if service fit in there, if not remove it
        # the service MUST fit sequentially
        # list of remain hours of the businessday
        remain_hours = businessday.get_remain_hours_list()
        service_start = datetime.datetime.combine(order_of_service.date, order_of_service.time)
        service_end = (service_start + datetime.timedelta(minutes=order_of_service.type_of_service.time))
        # list of the hours occupied by service
        service_hours = datetime_range(service_start, service_end, datetime.timedelta(minutes=settings.SLICE_OF_TIME))
        # must put the service_hours with remain_hours to allow check for sequential
        remain_hours.extend(service_hours)
        tupple_hours = []
        # print(f"Remain Hours: {remain_hours}")
        # check if is consecutive
        for rh in remain_hours:
            # start of service that is equal to the remain hour
            start = rh
            # the estimate end of service
            end = (start + datetime.timedelta(minutes=order_of_service.type_of_service.time))
            # make a list with the hours that the service need in base of remain hours
            # if rh is 09:00 and the service needs 60min (2 slices) the h_list is:
            # [09:00 (rh), 09:30]
            # if rh is 09:00 and the service needs 90min (3 slices) the h_list is:
            # [09:00 (rh), 09:30, 10:00]
            # So the h_list is all the hours (times) that the service occupy
            h_list = datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME))
            # print(f"H_LIST of {rh} : {[h for h in h_list]}")
            # print(f"REMAIN HOURS : {[h for h in remain_hours]}")
            f = True  # add this time?
            for h in h_list:
                # if one of the hour in h_list is not in remain_hours, so this rh is not compatible
                if h not in remain_hours:
                    f = False
            if f:
                tupple_hours.append((rh.strftime('%H:%M'), rh.strftime('%H:%M')))
        response = tupple_hours
        # print(response)
    # print(len(response), response)
    return len(response) > 0
