#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 15:56.
from datetime import datetime
from typing import Dict, Any

from business.models import BusinessDay
from config.models import StatusService, TypeOfService
from django.contrib.admin.utils import NestedObjects
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from .conf import *
from .forms import *
from .tables import *


@login_required
@require_http_methods(["GET"])
def get_order_of_service(request, pk):
    return render(request, 'homepage_perfil/service.html', {
        'obj': get_object_or_404(OrderOfService, pk=pk),
    })


@login_required
@require_http_methods(["GET", "POST"])
def create_order_of_service(request, d, m, y):
    """
    User (client) create a order of service from frontend when clicked on calendar
    :param request:
    :param d: day
    :param m: month
    :param y: year
    :return: a correspond view
    """
    template = 'homepage_perfil/schedule_service.html'
    s_date = datetime(y, m, d)
    business_day = get_object_or_404(BusinessDay, day=s_date)
    query_tp_s = TypeOfService.objects.filter(time__lte=business_day.get_remain_hours())
    times = business_day.get_tuple_remain_hours()
    if request.method == "GET":
        form = OrderOfServiceFormFrontend(query_tp_s=query_tp_s,
                                          times=times,
                                          businessday_pk=business_day.pk,
                                          initial={'date': s_date})
        return render(request, template_name=template, context={
            'date': s_date.date(),
            'form': form,
            'hours': business_day
        })
    else:
        with transaction.atomic():
            form = OrderOfServiceFormFrontend(request.POST,
                                              query_tp_s=query_tp_s,
                                              times=times,
                                              businessday_pk=business_day.pk)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.status = get_object_or_404(StatusService, pk=settings.STATUS_SERVICE_DEFAULT)
                instance.customer = request.user
                instance.save()
                return HttpResponseRedirect(reverse('users:frontend:profile'))
        return render(request, template_name=template, context={
            'date': s_date.date(),
            'form': form,
            'hours': business_day,
        })


@login_required
@require_http_methods(["GET"])
@transaction.atomic()
@permission_required('service.edit_orderofservice', raise_exception=True)
def cancel_order_of_service_admin(request, pk):
    """
    Cancel a order of service from admin
    :param request:
    :param pk: order of service
    :return: redirect to abosulute url (maybe profile)
    """
    instance = get_object_or_404(OrderOfService, pk=pk)
    instance.canceled = True
    instance.save()
    return redirect(instance.get_absolute_url())


@login_required
@require_http_methods(["GET"])
@transaction.atomic()
def cancel_order_of_service_frontend(request, pk):
    """
    Cancel a order of service from frontend, client is canceling
    :param request:
    :param pk: order of service
    :return: redirect to profile or permission denied if user is not owner of service
    """
    instance = get_object_or_404(OrderOfService, pk=pk)
    if instance.customer == request.user:
        instance.canceled = True
        instance.save()
        return redirect('users:frontend:profile')
    else:
        raise PermissionDenied()


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('service.edit_orderofservice', raise_exception=True)
def change_date_order_of_service(request):
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


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('service.edit_orderofservice', raise_exception=True)
def confirm_order_of_service(request, pk, flag):
    """
    Set an order of service to confirmed
    :param request:
    :param pk: pk of an order of service
    :param flag: used to tell where to redirect, 0 to profile and 1 to owner user
    :return:
    """
    instance = get_object_or_404(OrderOfService, pk=pk)
    instance.confirmed = True
    instance.save()
    return redirect(instance.get_absolute_url() if flag == 0 else instance.get_back_url())


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('service.edit_orderofservice', raise_exception=True)
def finish_order_of_service(request, pk, flag):
    """
    Set an order of service to confirmed
    :param request:
    :param pk: pk of an order of service
    :param flag: used to tell where to redirect, 0 to profile and 1 to owner user
    :return:
    """
    instance = get_object_or_404(OrderOfService, pk=pk)
    instance.status = get_object_or_404(StatusService, pk=settings.STATUS_SERVICE_FINISHED)
    instance.finished = True
    instance.save()
    return redirect(instance.get_absolute_url() if flag == 0 else instance.get_back_url())


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('service.view_orderofservice', raise_exception=True)
def profile_order_of_service(request, cpk, pk):
    """
    Rendering the profile of an order of service
    :param request:
    :param cpk: customer pk
    :param pk: order of service
    :return:
    """
    return render(request, 'service/profile.html', {'obj': OrderOfService.objects.get(pk=pk)})


class OrderOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
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
            return reverse('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

    def get_back_url(self):
        return reverse('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = User.objects.get(pk=self.kwargs['cpk'])
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
        return reverse_lazy('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
