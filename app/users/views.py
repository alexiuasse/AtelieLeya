#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/09/2020 13:01.
from typing import Dict, Any

from config.models import Reward, TypeOfService
from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, LazyPaginator
from frontend.apexcharts.simple_pie import SimplePie

from .conf import *
from .filters import *
from .forms import *
from .models import *
from .tables import *


@login_required
@require_http_methods(["GET"])
@staff_member_required()
@permission_required('users.get_profile', raise_exception=True)
def profile_admin(request, pk):
    user = User.objects.get(pk=pk)
    services = user.orderofservice_set.filter(customer=user, status=settings.STATUS_SERVICE_FINISHED)
    type_of_services = TypeOfService.objects.filter(pk__in=services.values_list('type_of_service', flat=True))
    rewards = user.rewardretrieved_set.all()
    rewards_type = Reward.objects.filter(pk__in=rewards.values_list('reward', flat=True))
    return render(request, template_name='user/profile.html', context={
        'obj': user.profile,
        'options_chart_service': SimplePie(
            series=[services.filter(type_of_service=t).count() for t in type_of_services],
            colors=[t.contextual for t in type_of_services],
            labels=[t.name for t in type_of_services],
        ).get_options(),
        'options_chart_reward': SimplePie(
            series=[rewards.filter(reward=r).count() for r in rewards_type],
            colors=[r.contextual for r in rewards_type],
            labels=[r.name for r in rewards_type],
        ).get_options(),
    })


class ProfileList(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Profile
    table_class = ProfileTable
    filterset_class = ProfileFilter
    paginator_class = LazyPaginator
    permission_required = ('users.view_profile',)
    template_name = 'user/list.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER
    back_url = reverse_lazy('frontend:dashboard')

    def get_queryset(self):
        return Profile.objects.filter(user__is_superuser=False).order_by('name')


class ProfileEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileFormAdmin
    template_name = 'user/form.html'
    permission_required = ('users.edit_profile',)
    title = TITLE_EDIT_USER
    subtitle = SUBTITLE_USER


# login_url='/accounts/login/'
@login_required
@require_http_methods(["GET"])
def profile_frontend(request):
    return render(request, "homepage/profile.html", {'start_date': datetime.today().date})


@login_required
@transaction.atomic
def profile_update(request):
    if request.method == 'POST':
        user_form = UserChangeFormFrontend(request.POST, instance=request.user)
        profile_form = ProfileFormFrontend(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:frontend:profile')
    else:
        user_form = UserChangeFormFrontend(instance=request.user)
        profile_form = ProfileFormFrontend(instance=request.user.profile)
    return render(request, 'homepage/signup_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationFormFrontend(request.POST)
        profile_form = ProfileFormFrontend(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile_form = ProfileFormFrontend(request.POST, instance=user.profile)
            if profile_form.is_valid():
                profile_form.save()
                username = user_form.cleaned_data.get('username')
                raw_password = user_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('users:frontend:profile')
    else:
        user_form = UserCreationFormFrontend()
        profile_form = ProfileFormFrontend()
    return render(request, 'homepage/signup_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


########################################################################################################################

@login_required
@require_http_methods(["GET"])
def reward_frontend(request):
    return render(request, template_name='homepage/reward_retrieve.html', context={
        'rewards': Reward.objects.filter(available=True),
    })


@login_required
@require_http_methods(["GET"])
def reward_retrieve_frontend(request, rpk):
    reward = get_object_or_404(Reward, pk=rpk)
    RewardRetrieved(
        reward=reward,
        points=reward.quantity_in_points,
        customer=request.user,
    ).save()
    request.user.profile.total_of_points -= reward.quantity_in_points
    request.user.save()
    return redirect('users:frontend:profile')


@login_required
@require_http_methods(["GET"])
@staff_member_required()
@permission_required('users.edit_rewardretrieved', raise_exception=True)
def reward_retrieved_confirm(request, pk):
    reward = get_object_or_404(RewardRetrieved, pk=pk)
    reward.retrieved = True
    reward.save()
    return HttpResponseRedirect(reward.customer.profile.get_absolute_url())


class RewardRetrievedList(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = RewardRetrieved
    table_class = RewardRetrievedTable
    filterset_class = RewardRetrievedFilter
    paginator_class = LazyPaginator
    permission_required = ('users.view_rewardretrieved',)
    template_name = 'reward/list.html'
    title = TITLE_VIEW_USER
    subtitle = SUBTITLE_USER
    back_url = reverse_lazy('frontend:dashboard')

    def get_queryset(self):
        return RewardRetrieved.objects.filter(retrieved=False).order_by('-date')


class RewardRetrievedCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = RewardRetrieved
    form_class = RewardRetrievedForm
    template_name = 'reward/form.html'
    permission_required = ('users.create_rewardretrieved',)
    title = TITLE_CREATE_REWARDRETRIEVED
    subtitle = SUBTITLE_REWARDRETRIEVED

    def get_success_url(self):
        if self.object:
            return reverse_lazy(self.object.get_back_url())
        else:
            return reverse_lazy('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

    def get_back_url(self):
        return reverse_lazy('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            customer = User.objects.get(pk=self.kwargs['cpk'])
            points = instance.reward.quantity_in_points * instance.quantity
            if points > customer.profile.total_of_points:
                form.add_error('reward',
                               f'Pontos Insuficientes! Faltando: {points - customer.profile.total_of_points} pts')
                return self.render_to_response(self.get_context_data(form=form))
            else:
                instance.customer = customer
                instance.points = points
                instance.save()
                customer.profile.total_of_points -= instance.points
                customer.profile.save()
                return HttpResponseRedirect(self.get_success_url())


class RewardRetrievedEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RewardRetrieved
    form_class = RewardRetrievedForm
    template_name = 'reward/form.html'
    permission_required = ('users.edit_rewardretrieved',)
    title = TITLE_EDIT_REWARDRETRIEVED
    subtitle = SUBTITLE_REWARDRETRIEVED

    def get_success_url(self):
        return reverse_lazy('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            profile = User.objects.get(pk=self.kwargs['cpk']).profile
            points = instance.reward.quantity_in_points * instance.quantity
            if points > profile.total_of_points:
                form.add_error('reward', f'Pontos Insuficientes! Faltando: {points - profile.total_of_points} pts')
                return self.render_to_response(self.get_context_data(form=form))
            else:
                instance.points = points
                instance.save()
                profile.total_of_points -= instance.points
                profile.save()
            return HttpResponseRedirect(self.get_success_url())


class RewardRetrievedDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = RewardRetrieved
    template_name = "reward/confirm_delete.html"
    permission_required = ('users.del_rewardretrieved',)
    title = TITLE_DEL_REWARDRETRIEVED
    subtitle = SUBTITLE_REWARDRETRIEVED

    def get_success_url(self):
        return reverse_lazy('users:admin:profile', kwargs={'pk': self.kwargs['cpk']})

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
        self.object.customer.profile.total_of_points += self.object.points
        self.object.customer.profile.save()
        self.object.delete()
        return HttpResponseRedirect(success_url)
