#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/08/2020 09:08.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin
from service.models import OrderOfService

from .conf import *
from .filters import *
from .forms import *
from .tables import *


class Config(LoginRequiredMixin, View):
    template = 'config/view.html'
    title = 'Configurações'
    subtitle = 'Configuração do sistema'

    def get(self, request):
        links = {
            'Brinde': {
                'reward': {
                    'name': "Brinde",
                    'link': reverse_lazy('config:reward:view'),
                    'count': Reward.objects.count(),
                },
            },
            'Serviços': {
                'status_service': {
                    'name': "Status do Serviço",
                    'link': reverse_lazy('config:statusservice:view'),
                    'count': StatusService.objects.count(),
                },
                'type_of_service': {
                    'name': "Tipo de Serviço",
                    'link': reverse_lazy('config:typeofservice:view'),
                    'count': TypeOfService.objects.count(),
                },
            },
            'Financeiro': {
                'reward': {
                    'name': "Tipo de Pagamento",
                    'link': reverse_lazy('config:typeofpayment:view'),
                    'count': TypeOfPayment.objects.count(),
                },
            },
        }
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'links': links
        }
        return render(request, self.template, context)


########################################################################################################################

class TypeOfPaymentView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = TypeOfPayment
    table_class = TypeOfPaymentTable
    filterset_class = TypeOfPaymentFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_typeofpayment'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_TYPE_OF_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_PAYMENT
    new = reverse_lazy('config:typeofpayment:create')
    back_url = reverse_lazy('config:index')


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
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_typeofpayment'
    success_url = reverse_lazy('config:typeofpayment:view')
    title = TITLE_DEL_CONFIG_TYPE_OF_PAYMENT
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_PAYMENT

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################
class TyperOfServiceGetValue(LoginRequiredMixin, View):

    def get(self, request, pk):
        order_of_service = get_object_or_404(OrderOfService, pk=pk)
        return JsonResponse({'value': order_of_service.type_of_service.value}, safe=False)


class TypeOfServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = TypeOfService
    table_class = TypeOfServiceTable
    filterset_class = TypeOfServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_typeofservice'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    new = reverse_lazy('config:typeofservice:create')
    back_url = reverse_lazy('config:index')


class TypeOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TypeOfService
    form_class = TypeOfServiceForm
    template_name = 'base/form.html'
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
    template_name = 'base/form.html'
    permission_required = 'config.edit_typeofservice'
    success_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_EDIT_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE


class TypeOfServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = TypeOfService
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_typeofservice'
    success_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_DEL_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
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
    permission_required = 'config.view_statuservice'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE
    new = reverse_lazy('config:statusservice:create')
    back_url = reverse_lazy('config:index')


class StatusServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StatusService
    form_class = StatusServiceForm
    template_name = 'base/form.html'
    permission_required = 'config.create_statuservice'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:statusservice:view')
    title = TITLE_CREATE_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE

    def get_back_url(self):
        return self.back_url


class StatusServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StatusService
    form_class = StatusServiceForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_statuservice'
    success_url = reverse_lazy('config:statusservice:view')
    title = TITLE_EDIT_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE


class StatusServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = StatusService
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_statusservice'
    success_url = reverse_lazy('config:statusservice:view')
    title = TITLE_DEL_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
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
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD
    new = reverse_lazy('config:reward:create')
    back_url = reverse_lazy('config:index')


class RewardCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Reward
    form_class = RewardForm
    template_name = 'base/form.html'
    permission_required = 'config.create_reward'
    back_url = reverse_lazy('config:reward:view')
    title = TITLE_CREATE_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD

    def get_back_url(self):
        return self.back_url


class RewardEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Reward
    form_class = RewardForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_reward'
    success_url = reverse_lazy('config:reward:view')
    title = TITLE_EDIT_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD


class RewardDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Reward
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_reward'
    success_url = reverse_lazy('config:reward:view')
    title = TITLE_DEL_CONFIG_REWARD
    subtitle = SUBTITLE_VIEW_CONFIG_REWARD

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context

########################################################################################################################
