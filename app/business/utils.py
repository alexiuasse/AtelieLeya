#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/09/2020 09:37.

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
