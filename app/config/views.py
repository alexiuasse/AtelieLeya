#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 23/09/2020 10:38.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin
from service.models import OrderOfService

from .conf import *
from .filters import *
from .forms import *
from .tables import *


class TypeOfPaymentView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = TypeOfPayment
    table_class = TypeOfPaymentTable
    filterset_class = TypeOfPaymentFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_typeofpayment'
    template_name = 'config/view.html'
    title = TITLE_VIEW_CONFIG_TYPE_OF_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_PAYMENT
    new = reverse_lazy('config:typeofpayment:create')
    back_url = reverse_lazy('frontend:dashboard')


class TypeOfPaymentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TypeOfPayment
    form_class = TypeOfPaymentForm
    template_name = 'config/form.html'
    permission_required = 'config.create_typeofpayment'
    back_url = reverse_lazy('config:typeofpayment:view')
    title = TITLE_CREATE_CONFIG_TYPE_OF_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_PAYMENT

    def get_back_url(self):
        return self.back_url


class TypeOfPaymentEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TypeOfPayment
    form_class = TypeOfPaymentForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_typeofpayment'
    success_url = reverse_lazy('config:typeofpayment:view')
    title = TITLE_EDIT_CONFIG_TYPE_OF_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_PAYMENT


class TypeOfPaymentDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = TypeOfPayment
    template_name = "config/confirm_delete.html"
    permission_required = 'config.del_typeofpayment'
    success_url = reverse_lazy('config:typeofpayment:view')
    title = TITLE_DEL_CONFIG_TYPE_OF_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_PAYMENT

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific dataconfig
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################
@login_required
@require_http_methods(["GET"])
@staff_member_required()
@permission_required('config.get_typeofservice', raise_exception=True)
def type_of_service_get_value(request, pk):
    """
    Used to get the value of a type of service when creating/editing an Invoice
    :param request:
    :param pk: type of service
    :return: JsonResponse with the value
    """
    return JsonResponse({'value': get_object_or_404(OrderOfService, pk=pk).type_of_service.value}, safe=False)


class TypeOfServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = TypeOfService
    table_class = TypeOfServiceTable
    filterset_class = TypeOfServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_typeofservice'
    template_name = 'config/view.html'
    title = TITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    new = reverse_lazy('config:typeofservice:create')
    back_url = reverse_lazy('frontend:dashboard')


class TypeOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TypeOfService
    form_class = TypeOfServiceForm
    template_name = 'config/form.html'
    permission_required = 'config.create_typeofservice'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_CREATE_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE

    def get_back_url(self):
        return self.back_url


class TypeOfServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TypeOfService
    form_class = TypeOfServiceForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_typeofservice'
    success_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_EDIT_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE


class TypeOfServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = TypeOfService
    template_name = "config/confirm_delete.html"
    permission_required = 'config.del_typeofservice'
    success_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_DEL_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific dataconfig
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class StatusServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = StatusService
    table_class = StatusServiceTable
    filterset_class = StatusServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_statusservice'
    template_name = 'config/view.html'
    title = TITLE_VIEW_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE
    new = reverse_lazy('config:statusservice:create')
    back_url = reverse_lazy('frontend:dashboard')


class StatusServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StatusService
    form_class = StatusServiceForm
    template_name = 'config/form.html'
    permission_required = 'config.create_statusservice'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:statusservice:view')
    title = TITLE_CREATE_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE

    def get_back_url(self):
        return self.back_url


class StatusServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StatusService
    form_class = StatusServiceForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_statusservice'
    success_url = reverse_lazy('config:statusservice:view')
    title = TITLE_EDIT_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE


class StatusServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = StatusService
    template_name = "config/confirm_delete.html"
    permission_required = 'config.del_statusservice'
    success_url = reverse_lazy('config:statusservice:view')
    title = TITLE_DEL_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific dataconfig
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class StatusPaymentView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = StatusPayment
    table_class = StatusPaymentTable
    filterset_class = StatusPaymentFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_statuspayment'
    template_name = 'config/view.html'
    title = TITLE_VIEW_CONFIG_STATUS_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_PAYMENT
    new = reverse_lazy('config:statuspayment:create')
    back_url = reverse_lazy('frontend:dashboard')


class StatusPaymentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StatusPayment
    form_class = StatusPaymentForm
    template_name = 'config/form.html'
    permission_required = 'config.create_statuspayment'
    back_url = reverse_lazy('config:statuspayment:view')
    title = TITLE_CREATE_CONFIG_STATUS_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_PAYMENT

    def get_back_url(self):
        return self.back_url


class StatusPaymentEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StatusPayment
    form_class = StatusPaymentForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_statuspayment'
    success_url = reverse_lazy('config:statuspayment:view')
    title = TITLE_EDIT_CONFIG_STATUS_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_PAYMENT


class StatusPaymentDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = StatusPayment
    template_name = "config/confirm_delete.html"
    permission_required = 'config.del_statuspayment'
    success_url = reverse_lazy('config:statuspayment:view')
    title = TITLE_DEL_CONFIG_STATUS_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_PAYMENT

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific dataconfig
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class RewardView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Reward
    table_class = RewardTable
    filterset_class = RewardFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_reward'
    template_name = 'config/view.html'
    title = TITLE_VIEW_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD
    new = reverse_lazy('config:reward:create')
    back_url = reverse_lazy('frontend:dashboard')


class RewardCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Reward
    form_class = RewardForm
    template_name = 'config/form.html'
    permission_required = 'config.create_reward'
    back_url = reverse_lazy('config:reward:view')
    title = TITLE_CREATE_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD

    def get_back_url(self):
        return self.back_url


class RewardEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Reward
    form_class = RewardForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_reward'
    success_url = reverse_lazy('config:reward:view')
    title = TITLE_EDIT_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD


class RewardDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Reward
    template_name = "config/confirm_delete.html"
    permission_required = 'config.del_reward'
    success_url = reverse_lazy('config:reward:view')
    title = TITLE_DEL_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific dataconfig
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class ExpedientView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Expedient
    table_class = ExpedientTable
    filterset_class = ExpedientFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_expedient'
    template_name = 'config/view.html'
    title = TITLE_VIEW_CONFIG_EXPEDIENT
    subtitle = SUBTITLE_VIEW_CONFIG_EXPEDIENT
    new = reverse_lazy('config:expedient:create')
    back_url = reverse_lazy('frontend:dashboard')


class ExpedientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Expedient
    form_class = ExpedientForm
    template_name = 'config/form.html'
    permission_required = 'config.create_expedient'
    back_url = reverse_lazy('config:expedient:view')
    title = TITLE_CREATE_CONFIG_EXPEDIENT
    subtitle = SUBTITLE_VIEW_CONFIG_EXPEDIENT

    def get_back_url(self):
        return self.back_url


class ExpedientEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Expedient
    form_class = ExpedientForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_expedient'
    success_url = reverse_lazy('config:expedient:view')
    title = TITLE_EDIT_CONFIG_EXPEDIENT
    subtitle = SUBTITLE_VIEW_CONFIG_EXPEDIENT


class ExpedientDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Expedient
    template_name = "config/confirm_delete.html"
    permission_required = 'config.del_expedient'
    success_url = reverse_lazy('config:expedient:view')
    title = TITLE_DEL_CONFIG_EXPEDIENT
    subtitle = SUBTITLE_VIEW_CONFIG_EXPEDIENT

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific dataconfig
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

@login_required
@require_http_methods(["GET"])
@staff_member_required()
@permission_required('config.view_homepage', raise_exception=True)
def homepage_view(request):
    if HomePage.objects.all().count() == 0:
        obj = HomePage(
            address="Adicionar Endereço",
            whatsapp='(00) 0 0000-0000',
        ).save()
    else:
        obj = HomePage.objects.first()
    return render(request, "config/homepage/homepage.html", {'obj': obj})


class HomePageEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = HomePage
    form_class = HomePageForm
    template_name = 'config/homepage/form.html'
    permission_required = 'config.edit_homepage'
    success_url = reverse_lazy('config:homepage:view')
    title = TITLE_EDIT_CONFIG_HOMEPAGE
    subtitle = SUBTITLE_VIEW_CONFIG_HOMEPAGE
