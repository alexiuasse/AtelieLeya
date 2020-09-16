#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 15/09/2020 10:06.

import logging

from config.models import Reward, TypeOfService
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .utils import *

logger = logging.getLogger(__name__)


def error_400(request, exception):
    logger.error("Error 400: [%s]" % exception)
    return render(request, '400.html', {}, status=400)


def error_401(request, exception):
    logger.error("Error 401: [%s]" % exception)
    return render(request, '401.html', {}, status=401)


def error_403(request, exception):
    logger.error("Error 403: [%s]" % exception)
    return render(request, '403.html', {}, status=403)


def error_404(request, exception):
    logger.error("Error 404: [%s]" % exception)
    return render(request, '404.html', {}, status=404)


def error_500(request):
    return render(request, '500.html', {}, status=500)


def error_503(request):
    return render(request, '503.html', {}, status=503)


@require_http_methods(["GET"])
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('users:frontend:profile' if not request.user.is_staff else 'frontend:dashboard')
        )
    else:
        return HttpResponseRedirect(reverse('frontend:homepage'))


@require_http_methods(["GET"])
def homepage(request):
    return render(request, 'homepage/homepage.html', {
        'rewards': Reward.objects.all(),
        'services': TypeOfService.objects.all(),
    })


@login_required
@staff_member_required()
@require_http_methods(["GET"])
def dashboard(request):
    return render(request, 'dashboard.html', context_dashboard())


@login_required
@staff_member_required()
@require_http_methods(["GET"])
def chart(request, year):
    return render(request, 'chart.html', context_chart(year))


@login_required
@require_http_methods(["GET"])
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('frontend:login'))
