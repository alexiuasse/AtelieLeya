#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 13/09/2020 13:12.

from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin

from .conf import *
from .filters import *
from .forms import *
from .models import *
from .tables import *


class WorkerProfileProfile(LoginRequiredMixin, View):
    template = 'worker/profile.html'
    title = TITLE_VIEW_WORKER_PROFILE
    subtitle = SUBTITLE_WORKER_PROFILE

    def get(self, request, pk):
        obj = get_object_or_404(WorkerProfile, pk=pk)
        return render(request, self.template, {
            'obj': obj
        })


class WorkerProfileView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = WorkerProfile
    table_class = WorkerProfileTable
    filterset_class = WorkerProfileFilter
    paginator_class = LazyPaginator
    permission_required = 'worker.view_workerprofile'
    template_name = 'user/view.html'
    title = TITLE_VIEW_WORKER_PROFILE
    subtitle = SUBTITLE_WORKER_PROFILE
    new = reverse_lazy('worker:workerprofile:create')
    back_url = reverse_lazy('frontend:dashboard')

    def get_queryset(self):
        return WorkerProfile.objects.all().order_by('customuser__first_name')


class WorkerProfileCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = WorkerProfile
    form_class = WorkerProfileForm
    template_name = 'worker/form.html'
    permission_required = 'worker.create_workerprofile'
    title = TITLE_CREATE_WORKER_PROFILE
    subtitle = SUBTITLE_WORKER_PROFILE

    def get_success_url(self):
        return self.object.get_absolute_url() if self.object else reverse_lazy('worker:workerprofile:view')

    @staticmethod
    def get_back_url():
        return reverse_lazy('worker:workerprofile:view')


class WorkerProfileEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = WorkerProfile
    form_class = WorkerProfileForm
    template_name = 'worker/form.html'
    permission_required = 'worker.edit_workerprofile'
    title = TITLE_EDIT_WORKER_PROFILE
    subtitle = SUBTITLE_WORKER_PROFILE


class WorkerProfileDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = WorkerProfile
    template_name = "worker/confirm_delete.html"
    permission_required = 'worker.del_workerprofile'
    success_url = reverse_lazy('worker:workerprofile:view')
    title = TITLE_DEL_WORKER_PROFILE
    subtitle = SUBTITLE_WORKER_PROFILE

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific datafinancial
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
