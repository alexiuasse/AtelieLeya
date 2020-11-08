#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 11:13.

import logging

from config.models import Reward, TypeOfService
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from homepage.models import HomePage

from .utils import *

logger = logging.getLogger(__name__)


def error_400(request, exception):
    logger.error("Error 400: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 400,
        'error_text': 'A sua requisição possui alguma coisa errada!',
    }, status=400)


def error_401(request, exception):
    logger.error("Error 401: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 401,
        'error_text': 'Você não possui autorização para acessar essa página!',
    }, status=401)


def error_403(request, exception):
    logger.error("Error 403: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 403,
        'error_text': 'Você não possui autorização para acessar essa página!',
    }, status=403)


def error_404(request, exception):
    logger.error("Error 404: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 404,
        'error_text': 'Página não foi encontrada!',
    }, status=404)


def error_500(request):
    return render(request, 'error.html', {
        'error_code': 500,
        'error_text': 'Aconteceu um erro interno no servidor!',
    }, status=500)


def error_503(request):
    return render(request, 'error.html', {
        'error_code': 503,
        'error_text': 'Nosso serviço não está disponível no momento!',
    }, status=503)


@require_http_methods(["GET"])
def wakeup(request):
    if 'X-Appengine-Cron' in request.headers and request.headers['X-Appengine-Cron']:
        status = 200
    else:
        status = 400
    return HttpResponse(status=status)


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
    if HomePage.objects.all().count() == 0:
        obj = HomePage(
            title="Atêlie Leya Monteiro",
            address="Adicionar Endereço",
            whatsapp='(00) 0 0000-0000',
        ).save()
    else:
        obj = HomePage.objects.first()
    return render(request, 'homepage/homepage.html', {
        'homepage': obj,
        'rewards': Reward.objects.all(),
        'services': TypeOfService.objects.all(),
    })


@require_http_methods(["GET"])
def maintenance(request):
    return render(request, 'maintenance.html', {})


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

# @login_required
# @require_http_methods(["GET"])
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('frontend:login'))
