#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 09:36.

from typing import Dict, Any

from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin, SingleTableView
from users.models import CustomUser
from config.models import StatusService

from .conf import *
from .filters import *
from .forms import *
from .tables import *


class OrderOfServiceChangeDate(LoginRequiredMixin, View):
    """
        View to easy change the date and time of an orderofservice from dashboard calendar
    """

    def get(self, request):
        status, error_message = True, ""
        pk = request.GET.get('pk', None)
        try:
            if pk:
                instance = get_object_or_404(OrderOfService, pk=pk)
                new_date, new_time = request.GET.get('date', None), request.GET.get('time', None)
                if new_date and new_time:
                    instance.date = new_date
                    instance.time = new_time
                    instance.save()
                else:
                    status, error_message = False, "Data ou Hora inválidos!"
            else:
                status, error_message = False, "Faltando informações: 'PK' "
        except Exception as e:
            status, error_message = False, "O seguinte erro aconteceu %s" % e
        return JsonResponse({
            'status': status,
            'error_message': error_message,
        })


class OrderOfServiceConfirmed(LoginRequiredMixin, View):
    """
        View to easy confirm orderofservice
    """

    def get(self, request, pk, flag):
        if request.user.is_superuser and request.user.is_authenticated:
            instance = get_object_or_404(OrderOfService, pk=pk)
            instance.confirmed = True
            instance.save()
            return redirect(
                instance.get_absolute_url() if flag == 0 else instance.get_back_url()
            )
        else:
            raise PermissionDenied()


class OrderOfServiceFinished(LoginRequiredMixin, View):
    """
        View to easy change the status of orderofservice to finished
    """

    def get(self, request, pk, flag):
        if request.user.is_superuser and request.user.is_authenticated:
            instance = get_object_or_404(OrderOfService, pk=pk)
            instance.status = get_object_or_404(StatusService, pk=settings.STATUS_SERVICE_FINISHED)
            instance.finished = True
            instance.save()
            return redirect(
                instance.get_absolute_url() if flag == 0 else instance.get_back_url()
            )
        else:
            raise PermissionDenied()


########################################################################################################################

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


########################################################################################################################

class OrderOfServiceProfile(LoginRequiredMixin, View):
    """
        Show one order of service given the pk
    """

    template = 'service/profile.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get(self, request, cpk, pk):
        return render(request, self.template, {'obj': OrderOfService.objects.get(pk=pk)})


# unused
class OrderOfServiceIndex(LoginRequiredMixin, SingleTableView):
    """
        View to show all orderofservices in a table
    """
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


# unused
class OrderOfServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = OrderOfService
    table_class = OrderOfServiceTable
    filterset_class = OrderOfServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'service.view_orderofservice'
    template_name = 'service/view.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    new = reverse_lazy('service:index')


class OrderOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
        Create new order of service from admin panel
    """

    model = OrderOfService
    form_class = OrderOfServiceForm
    template_name = 'service/form.html'
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
    template_name = 'service/form.html'
    permission_required = 'service.edit_orderofservice'
    title = TITLE_EDIT_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE


class OrderOfServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = OrderOfService
    template_name = "service/confirm_delete.html"
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
