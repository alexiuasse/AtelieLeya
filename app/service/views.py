#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 10:24.

from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin, SingleTableView
from users.models import CustomUser

from .conf import *
from .filters import *
from .forms import *
from .tables import *


def confirmed_service(request, cpk, pk):
    if request.user.is_superuser and request.user.is_authenticated:
        obj = OrderOfService.objects.get(pk=pk)
        obj.confirmed = True
        obj.save()
        return redirect(obj.get_absolute_url())
    else:
        raise PermissionDenied()


def finished_service(request, cpk, pk):
    if request.user.is_superuser and request.user.is_authenticated:
        obj = OrderOfService.objects.get(pk=pk)
        obj.finished = True
        obj.save()
        return redirect(obj.get_absolute_url())
    else:
        raise PermissionDenied()


class ServiceCalendarCustomer(LoginRequiredMixin, View):
    template = 'homepage/calendar.html'
    title = 'Agendamento Fácil'
    subtitle = 'Agende seu horário'

    def get(self, request):
        return render(request, self.template, {
            'start_date': datetime.today().date,
            'title': self.title,
            'subtitle': self.subtitle,
            'services': OrderOfService.objects.all()
        })


class ServiceCalendarAdmin(LoginRequiredMixin, View):
    template = 'service/calendar.html'
    title = 'Calendário Admin'
    subtitle = 'Serviços'

    def get(self, request):
        return render(request, self.template, {
            'start_date': datetime.today().date,
            'title': self.title,
            'subtitle': self.subtitle,
            'services': OrderOfService.objects.all()
        })


class OrderOfServiceProfile(LoginRequiredMixin, View):
    """
        Show one order of service given the pk
    """

    template = 'service/profile.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get(self, request, cpk, pk):
        return render(request, self.template, {'obj': OrderOfService.objects.get(pk=pk)})


class OrderOfServiceIndex(LoginRequiredMixin, SingleTableView):
    template_name = 'service/view.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    table_class = OrderOfServiceTable
    paginator_class = LazyPaginator

    def get_queryset(self):
        query = {'date__year': self.kwargs['year'], 'scheduled': self.kwargs['scheduled']}
        if self.kwargs['status'] != 0:
            query['status'] = self.kwargs['status']
        if self.kwargs['day'] != 0:
            query['date__day'] = self.kwargs['day']
        if self.kwargs['month'] != 0:
            query['date__month'] = self.kwargs['month']
        return OrderOfService.objects.filter(**query).order_by('-date')

    @staticmethod
    def get_back_url():
        return reverse_lazy('dashboard')


class OrderOfServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = OrderOfService
    table_class = OrderOfServiceTable
    filterset_class = OrderOfServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'service.view_orderofservice'
    template_name = 'base/view.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    new = reverse_lazy('service:index')


class OrderOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
        Create new order of service from admin panel
    """

    model = OrderOfService
    form_class = OrderOfServiceForm
    template_name = 'base/form.html'
    permission_required = 'service.create_orderofservice'
    title = TITLE_CREATE_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get_success_url(self):
        if self.object:
            return reverse(self.object.get_absolute_url())
        else:
            return reverse('users:customuser:profile', kwargs={'pk': self.kwargs['cpk']})

    def get_back_url(self):
        return reverse('users:customuser:profile', kwargs={'pk': self.kwargs['cpk']})

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = CustomUser.objects.get(pk=self.kwargs['cpk'])
            instance.save()
        return HttpResponseRedirect(self.get_success_url())


class OrderOfServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OrderOfService
    form_class = OrderOfServiceForm
    template_name = 'base/form.html'
    permission_required = 'service.edit_orderofservice'
    title = TITLE_EDIT_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get_delete_url(self):
        return reverse('service:orderofservice:delete', kwargs={'cpk': self.kwargs['cpk'], 'pk': self.object.pk})


class OrderOfServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = OrderOfService
    template_name = "base/confirm_delete.html"
    permission_required = 'service.del_orderofservice'
    title = TITLE_DEL_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get_success_url(self):
        return reverse_lazy('users:customuser:profile', kwargs={'pk': self.kwargs['cpk']})

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
