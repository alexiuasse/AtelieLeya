#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/08/2020 13:37.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.base import View
from frontend.icons import ICON_DASHBOARD

from .conf import *
from .forms import *
from .models import *


########################################################################################################################
def check_if_day_is_full(request):
    day = BusinessDay.objects.get(day=request.GET.get('date', None))
    return JsonResponse({
        'is_full': day.force_day_full if day.force_day_full else day.get_is_full(),
    })


def businessday_create(request):
    """
    Create businessday getting the start and end date from request and the rest from form
    :param request:
    :return:
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
            return redirect('frontend:dashboard')
    else:
        return redirect('frontend:dashboard')


########################################################################################################################
class BusinessCalendarView(LoginRequiredMixin, View):
    template = 'business/calendar.html'
    title = TITLE_VIEW_CALENDAR
    subtitle = SUBTITLE_CALENDAR

    def get(self, request):
        return render(request, self.template, {
            'config': {
                'title': {
                    'text': self.title,
                    'icon': ICON_DASHBOARD
                },
                'pre_title': self.subtitle,
            },
            'start_date': datetime.datetime.today().date,
            'form': BusinessDayForm(),
        })


class BusinessDayProfile(LoginRequiredMixin, View):
    template = 'business/profile.html'
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

class ExpedientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Expedient
    form_class = ExpedientForm
    template_name = 'business/form.html'
    permission_required = 'business.create_expedient'
    title = TITLE_CREATE_EXPEDIENT
    subtitle = SUBTITLE_EXPEDIENT

    def get_success_url(self):
        if self.object:
            return reverse(self.object.get_absolute_url())
        else:
            return reverse('frontend:dashboard')

    @staticmethod
    def get_back_url():
        return reverse('frontend:dashboard')


class ExpedientEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Expedient
    form_class = ExpedientForm
    template_name = 'business/form.html'
    permission_required = 'business.edit_expedient'
    title = TITLE_CREATE_EXPEDIENT
    subtitle = SUBTITLE_EXPEDIENT


class ExpedientDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Expedient
    template_name = "business/confirm_delete.html"
    permission_required = 'business.del_expedient'
    title = TITLE_CREATE_EXPEDIENT
    subtitle = SUBTITLE_EXPEDIENT

    def get_success_url(self):
        return reverse_lazy('frontend:dashboard')

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
