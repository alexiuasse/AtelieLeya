#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/09/2020 14:19.
from typing import Dict, Any

from config.models import Reward
from config.models import TypeOfService
from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.base import View
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, LazyPaginator
from frontend.apexcharts.simple_pie import SimplePie

from .conf import *
from .filters import *
from .forms import *
from .models import *
from .tables import *


class RewardRetrieveFrontend(LoginRequiredMixin, View):
    template = 'homepage/reward_retrieve.html'
    title = "Brindes"
    subtitle = "Resgate seus brindes"

    def get(self, request):
        rewards = Reward.objects.filter(available=True)
        return render(request, self.template, {
            'obj': request.user,
            'rewards': rewards,
        })


class CustomUserProfileFrontend(LoginRequiredMixin, View):
    """
        Show one user given the pk
    """

    template = 'homepage/profile.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER

    def get(self, request):
        obj = request.user
        return render(request, self.template, {
            'obj': obj,
            'start_date': datetime.today().date
        })


class CustomUserProfileAdmin(LoginRequiredMixin, View):
    """
        Show one user given the pk
    """

    template = 'user/profile.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER

    def get(self, request, pk):
        obj = CustomUser.objects.get(pk=pk)
        services = obj.orderofservice_set.filter(customer=obj, status=settings.STATUS_SERVICE_FINISHED)
        type_of_services = TypeOfService.objects.filter(pk__in=services.values_list('type_of_service', flat=True))
        rewards = obj.rewardretrieved_set.all()
        rewards_type = Reward.objects.filter(pk__in=rewards.values_list('reward', flat=True))
        return render(request, self.template, {
            'obj': obj,
            'options_chart_service': SimplePie(
                # title='Procedimentos',
                series=[services.filter(type_of_service=t).count() for t in type_of_services],
                colors=[t.contextual for t in type_of_services],
                labels=[t.name for t in type_of_services],
            ).get_options(),
            'options_chart_reward': SimplePie(
                # title='Procedimentos',
                series=[rewards.filter(reward=r).count() for r in rewards_type],
                colors=[r.contextual for r in rewards_type],
                labels=[r.name for r in rewards_type],
            ).get_options(),
        })


class CustomUserView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = CustomUser
    table_class = CustomUserTable
    filterset_class = CustomUserFilter
    paginator_class = LazyPaginator
    permission_required = 'users.view_customuser'
    template_name = 'user/view.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER
    new = reverse_lazy('users:customuser:create')
    back_url = reverse_lazy('frontend:dashboard')

    def get_queryset(self):
        return CustomUser.objects.filter(is_superuser=False).order_by('first_name')


class CustomUserCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
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


class CustomUserEditFrontend(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeFrontendForm
    template_name = 'homepage/editform.html'
    title = TITLE_EDIT_USER
    subtitle = SUBTITLE_USER

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:customuser:profile_frontend')


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


def signup_frontend(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users:customuser:profile_frontend')
    else:
        form = SignUpForm()
    return render(request, 'homepage/signup.html', {'form': form})


########################################################################################################################
def rewardretrieved_create(request, rpk):
    if request.user.is_authenticated and request.method == 'GET':
        reward = get_object_or_404(Reward, pk=rpk)
        RewardRetrieved(
            reward=reward,
            points=reward.quantity_in_points,
            customer=request.user,
        ).save()
        request.user.total_of_points -= reward.quantity_in_points
        request.user.save()
        return redirect('users:customuser:profile_frontend')
    else:
        raise PermissionDenied()


class RewardRetrievedCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = RewardRetrieved
    form_class = RewardRetrievedForm
    template_name = 'base/form.html'
    permission_required = 'users.create_rewardretrieved'
    title = TITLE_CREATE_REWARDRETRIEVED
    subtitle = SUBTITLE_REWARDRETRIEVED

    def get_success_url(self):
        if self.object:
            return reverse_lazy(self.object.get_back_url())
        else:
            return reverse_lazy('users:customuser:profile_admin', kwargs={'pk': self.kwargs['cpk']})

    def get_back_url(self):
        return reverse_lazy('users:customuser:profile_admin', kwargs={'pk': self.kwargs['cpk']})

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            customer = CustomUser.objects.get(pk=self.kwargs['cpk'])
            points = instance.reward.quantity_in_points * instance.quantity
            if points > customer.total_of_points:
                form.add_error('reward', f'Pontos Insuficientes! Faltando: {points - customer.total_of_points} pts')
                return self.render_to_response(self.get_context_data(form=form))
            else:
                instance.customer = customer
                instance.points = points
                instance.save()
                customer.total_of_points -= instance.points
                customer.save()
                return HttpResponseRedirect(self.get_success_url())


class RewardRetrievedEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RewardRetrieved
    form_class = RewardRetrievedForm
    template_name = 'base/form.html'
    permission_required = 'users.edit_rewardretrieved'
    title = TITLE_EDIT_REWARDRETRIEVED
    subtitle = SUBTITLE_REWARDRETRIEVED

    def get_success_url(self):
        return reverse_lazy('users:customuser:profile_admin', kwargs={'pk': self.kwargs['cpk']})

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            customer = CustomUser.objects.get(pk=self.kwargs['cpk'])
            points = instance.reward.quantity_in_points * instance.quantity
            if points > customer.total_of_points:
                form.add_error('reward', f'Pontos Insuficientes! Faltando: {points - customer.total_of_points} pts')
                return self.render_to_response(self.get_context_data(form=form))
            else:
                instance.points = points
                instance.save()
                customer.total_of_points -= instance.points
                customer.save()
            return HttpResponseRedirect(self.get_success_url())


class RewardRetrievedDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = RewardRetrieved
    template_name = "service/confirm_delete.html"
    permission_required = 'users.del_rewardretrieved'
    title = TITLE_DEL_REWARDRETRIEVED
    subtitle = SUBTITLE_REWARDRETRIEVED

    def get_success_url(self):
        return reverse_lazy('users:customuser:profile_admin', kwargs={'pk': self.kwargs['cpk']})

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.customer.total_of_points += self.object.points
        self.object.customer.save()
        self.object.delete()
        return HttpResponseRedirect(success_url)


########################################################################################################################

class CalendarFrontend(LoginRequiredMixin, View):
    template = 'homepage/calendar.html'

    def get(self, request):
        return render(request, self.template, {
            'start_date': datetime.today().date
        })
