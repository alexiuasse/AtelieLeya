#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/08/2020 09:55.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.base import View
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, LazyPaginator

from .conf import *
from .filters import *
from .forms import *
from .tables import *


class CustomUserProfile(LoginRequiredMixin, View):
    """
        Show one user given the pk
    """

    template = 'user/profile.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER

    def get(self, request, pk):
        return render(request, self.template, {'obj': CustomUser.objects.get(pk=pk)})


class CustomUserCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
        Create new order of service from admin panel
    """

    model = CustomUser
    form_class = SignUpForm
    template_name = 'user/form.html'
    permission_required = 'service.create_orderofservice'
    title = TITLE_CREATE_USER
    subtitle = SUBTITLE_USER

    def get_success_url(self):
        return self.object.get_absolute_url() if self.object else reverse_lazy('users:customuser:view')

    @staticmethod
    def get_back_url():
        return reverse_lazy('users:customuser:view')


class CustomUserView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = CustomUser
    table_class = CustomUserTable
    filterset_class = CustomUserFilter
    paginator_class = LazyPaginator
    permission_required = 'users.view_customuser'
    template_name = 'base/view.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER
    new = reverse_lazy('users:customuser:create')
    back_url = reverse_lazy('frontend:dashboard')

    def get_queryset(self):
        return CustomUser.objects.filter(is_superuser=False)


class CustomUserEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'user/form.html'
    permission_required = 'users.edit_customuser'
    title = TITLE_EDIT_USER
    subtitle = SUBTITLE_USER

    def get_delete_url(self):
        return reverse_lazy('users:customuser:delete', kwargs={'pk': self.object.pk})


class CustomUserDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "base/confirm_delete.html"
    permission_required = 'users.del_customuser'
    title = TITLE_DEL_USER
    subtitle = SUBTITLE_USER

    def get_success_url(self):
        return reverse_lazy('users:customuser:view')

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})
