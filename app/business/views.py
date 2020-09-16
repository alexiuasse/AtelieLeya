#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 09:37.
from typing import Dict, Any

from config.models import TypeOfService
from django.contrib.admin.utils import NestedObjects
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, DeleteView
from django.views.generic.base import View
from frontend.icons import ICON_CALENDAR

from .conf import *
from .forms import *
from .models import *


########################################################################################################################

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


@login_required
@require_http_methods(["GET"])
def businessday_get_hours(request, pk, bpk):
    """
    Check if a Type Of Service fit in the businessday, called from client schedule service
    :param request:
    :param pk: type of service
    :param bpk: bussinesday
    :return: JsonResponse with the hours, Empty if not exists
    """
    type_of_service = get_object_or_404(TypeOfService, pk=pk)
    slices = type_of_service.time / settings.SLICE_OF_TIME  # how many slices is need for this service
    businessday = get_object_or_404(BusinessDay, pk=bpk)
    data = businessday.get_tuple_remain_hours()
    if slices > 1:
        # for each available hours, check if service fit in there, if not remove it
        # the service MUST fit sequentially
        remain_hours = businessday.get_remain_hours_list()  # list of remain hours
        tupple_hours = []
        # check if is consecutive
        for rh in remain_hours:
            start = rh
            end = (rh + datetime.timedelta(minutes=type_of_service.time))
            # hours that the service need
            h_list = datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME))
            f = True  # add this time?
            for h in h_list:
                if h not in remain_hours:
                    f = False
            if f:
                tupple_hours.append((rh.strftime('%H:%M'), rh.strftime('%H:%M')))
        data = tupple_hours

    return JsonResponse(
        data=data,
        safe=False
    )


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('business.create_businessday', 'business.edit_businessday', raise_exception=True)
def businessday_create(request):
    """
    Create businessday getting the start and end date from request and the rest from form, called from calendar admin
    :param request:
    :return: redirect to page
    """
    form = BusinessDayForm(request.POST)
    if form.is_valid():
        start = datetime.datetime.strptime(form['start'].value(), "%Y-%m-%d")
        end = datetime.datetime.strptime(form['end'].value(), "%Y-%m-%d")
        with transaction.atomic():
            dates = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
            for d in dates:
                try:
                    instance = BusinessDay.objects.get(day=d)
                    instance.color = form['color'].value()
                    instance.is_work_day = form['is_work_day'].value()
                    instance.force_day_full = form['force_day_full'].value()
                    instance.save()
                    instance.expedient_day.clear()
                    instance.expedient_day.add(*form['expedient_day'].value())
                except BusinessDay.DoesNotExist:
                    instance = BusinessDay(
                        day=d,
                        color=form['color'].value(),
                        is_work_day=form['is_work_day'].value(),
                        force_day_full=form['force_day_full'].value(),
                    )
                    instance.save()
                    instance.expedient_day.add(*form['expedient_day'].value())
            return redirect('business:calendar:view')
    else:
        return redirect('business:calendar:view')


########################################################################################################################
class BusinessCalendarView(LoginRequiredMixin, PermissionRequiredMixin, View):
    template = 'business/calendar.html'
    permission_required = 'business.view_businessday'
    title = TITLE_VIEW_CALENDAR
    subtitle = SUBTITLE_CALENDAR

    def get(self, request):
        return render(request, self.template, {
            'config': {
                'title': {
                    'text': self.title,
                    'icon': ICON_CALENDAR
                },
                'pre_title': self.subtitle,
            },
            'start_date': datetime.datetime.today().date,
            'form': BusinessDayForm(),
        })


class BusinessDayProfile(LoginRequiredMixin, PermissionRequiredMixin, View):
    template = 'business/profile.html'
    permission_required = 'business.view_businessday'
    title = TITLE_EDIT_BUSINESS_DAY
    subtitle = SUBTITLE_BUSINESS_DAY

    def get(self, request, pk):
        return render(request, self.template, {'obj': BusinessDay.objects.get(pk=pk)})


class BusinessDayEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BusinessDay
    form_class = BusinessDayForm
    template_name = 'business/form.html'
    permission_required = 'business.edit_businessday'
    title = TITLE_EDIT_BUSINESS_DAY
    subtitle = SUBTITLE_BUSINESS_DAY


class BusinessDayDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = BusinessDay
    template_name = "business/confirm_delete.html"
    permission_required = 'business.del_businessday'
    title = TITLE_EDIT_BUSINESS_DAY
    subtitle = SUBTITLE_BUSINESS_DAY

    def get_success_url(self):
        return reverse_lazy('frontend:dashboard')

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context

########################################################################################################################
