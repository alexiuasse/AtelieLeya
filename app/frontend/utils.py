#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/09/2020 21:10.
from datetime import datetime

from config.models import TypeOfService, StatusPayment, Reward
from django.contrib.auth.models import User
from financial.models import Invoice
from frontend.icons import ICON_COIN, ICON_PERSON, ICON_WAND, ICON_GIFT, ICON_CALENDAR, ICON_TRIANGLE_ALERT, \
    ICON_LINE_CHART
from service.models import OrderOfService
from users.models import RewardRetrieved, Profile

from .apexcharts.line import Line
from .apexcharts.simple_pie import SimplePie


def context_dashboard():
    today = datetime.today()
    birthdays = Profile.objects.filter(birth_date__day=today.day, birth_date__month=today.month)
    services_today = OrderOfService.objects.filter(date=today)
    services_not_confirmed = OrderOfService.objects.filter(confirmed=False)
    services_invoice_not_completed = [obj for obj in OrderOfService.objects.all() if obj.is_invoice_not_completed()]
    rewards_not_retrieved = RewardRetrieved.objects.filter(retrieved=False).order_by('-date')

    order_of_service_year = OrderOfService.objects.filter(date__year=today.year)
    reward_retrieved_year = RewardRetrieved.objects.filter(date__year=today.year)
    # row deck in top page
    top_row_deck = {
        'card_1': {
            'title': f'{Profile.objects.filter(user__date_joined__year=today.year).count()} Clientes registrados',
            'subtitle': f'{Profile.objects.filter(user__date_joined=today).count()} registrados hoje.',
            'icon': ICON_PERSON,
            'bg_color': 'bg-blue',
        },
        'card_2': {
            'title': f'{order_of_service_year.count()} Procedimentos',
            'subtitle': f'{services_today.count()} agendados para hoje.',
            'icon': ICON_WAND,
            'bg_color': 'bg-green',
        },
        'card_3': {
            'title': f'{reward_retrieved_year.filter(retrieved=True).count()} Brindes Resgatados',
            'subtitle': f'{reward_retrieved_year.filter(retrieved=False).count()} em espera.',
            'icon': ICON_GIFT,
            'bg_color': 'bg-pink',
        },
    }

    birthdays_row_card = {
        'title': 'Aniversariantes',
        'subtitle': 'Clientes Que Fazem Aniversário.',
        'icon': ICON_GIFT,
        'data': birthdays,
    }

    services_row_card = {
        'title': 'Procedimentos',
        'subtitle': 'Procedimentos Agendados.',
        'icon': ICON_WAND,
        'data': services_today,
    }

    service_not_confirmed_row_card = {
        'title': 'Procedimentos',
        'subtitle': 'Procedimentos que ainda não foram confirmados.',
        'icon': ICON_WAND,
        'data': services_not_confirmed,
    }

    service_not_completed_row_card = {
        'title': 'Procedimentos',
        'subtitle': 'Procedimentos com fatura incompleta.',
        'icon': ICON_COIN,
        'data': services_invoice_not_completed,
    }

    rewards_not_retrieved_row_card = {
        'title': 'Brindes',
        'subtitle': 'Brindes não retirados.',
        'icon': ICON_GIFT,
        'data': rewards_not_retrieved,
    }

    return {
        'year': today.year,
        'today': today.date(),
        'top_row_deck': top_row_deck,
        'birthdays_row_card': birthdays_row_card,
        'services_row_card': services_row_card,
        'service_not_confirmed_row_card': service_not_confirmed_row_card,
        'service_not_completed_row_card': service_not_completed_row_card,
        'rewards_not_retrieved_row_card': rewards_not_retrieved_row_card,
    }


def context_chart(req_year):
    year = datetime.today().year if not req_year else req_year

    config = {
        'pre_title': f'Gráficos do ano {year}',
        'title': {
            'text': 'Gráficos',
            'icon': ICON_LINE_CHART,
        }
    }

    line_charts = {
        'customers': {
            'chart_line': {
                'id': 'chart-customers',
                'class': 'chart',
                'description': 'Quantidade de clientes registrados separados mensalmente.',
                'config': {
                    'col': 'col-lg-8',
                },
                'title': {
                    'text': 'Ganho de Clientes',
                    'icon': ICON_PERSON,
                },
            },
            'chart_pie': {
                'id': 'chart-reward',
                'class': 'chart',
                'description': 'Visualização de brindes resgatados.',
                'config': {
                    'col': 'col-lg-4',
                },
                'title': {
                    'text': 'Brindes',
                    'icon': ICON_GIFT,
                },
            },
        },
        'services_finished': {
            'chart_line': {
                'id': 'chart-services-finished',
                'class': 'chart',
                'description': 'Procedimentos que foram finalizados.',
                'config': {
                    'col': 'col-lg-8',
                },
                'title': {
                    'text': 'Procedimentos Finalizados',
                    'icon': ICON_WAND,
                },
            },
            'chart_pie': {
                'id': 'chart-services-pie',
                'class': 'chart',
                'description': 'Visualização de procedimentos finalizados.',
                'config': {
                    'col': 'col-lg-4',
                },
                'title': {
                    'text': 'Divisão por Procedimento',
                    'icon': ICON_WAND,
                },
            },
        },
        'financials': {
            'chart_line': {
                'id': 'chart-financial',
                'class': 'chart',
                'description': 'Valor em R$ mensal separado por status que se encontram.',
                'config': {
                    'col': 'col-lg-8',
                },
                'title': {
                    'text': 'Rendimento Mensal',
                    'icon': ICON_COIN,
                },
            },
            'chart_pie': {
                'id': 'chart-financial-pie',
                'class': 'chart',
                'description': 'Divisão por status das faturas.',
                'config': {
                    'col': 'col-lg-4',
                },
                'title': {
                    'text': 'Divisão por Status de Faturas',
                    'icon': ICON_COIN,
                },
            },
        },
    }

    charts = {
        'chart-customers': {
            'options': Line(
                x_title='Mês',
                y_title='Quantidade',
                series=[{
                    'data': [
                        User.objects.filter(date_joined__month=month, date_joined__year=year).count()
                        for month in range(1, 13)
                    ],
                    'name': 'Clientes',
                }],
                colors=['#206bc4'],
            ).get_options(),
        },
        # REWARD
        'chart-reward': {
            'options': SimplePie(
                series=[
                    RewardRetrieved.objects.filter(date__year=year, reward=r.pk).count()
                    for r in Reward.objects.all()
                ],
                colors=[r.contextual for r in Reward.objects.all()],
                labels=[r.name for r in Reward.objects.all()],
            ).get_options(),
        },
        # FINANCIAL
        'chart-financial': {
            'options': Line(
                x_title='Mês',
                y_title='Valor em R$',
                series=[get_financial_value(year, s) for s in StatusPayment.objects.all()],
                colors=[t.contextual for t in StatusPayment.objects.all()],
            ).get_options(),
        },
        'chart-financial-pie': {
            'options': SimplePie(
                # title=f'Divisão Por Status - Total ({Invoice.objects.filter(date__year=year).count()})',
                series=[Invoice.objects.filter(date__year=year, status=t.pk).count() for t in
                        StatusPayment.objects.all()],
                colors=[t.contextual for t in StatusPayment.objects.all()],
                labels=[t.name for t in StatusPayment.objects.all()],
            ).get_options(),
        },
        # SERVICE
        'chart-services-finished': {
            'options': Line(
                x_title='Mês',
                y_title='Quantidade',
                series=[get_series_service(year, t, True) for t in TypeOfService.objects.all()],
                colors=[t.contextual for t in TypeOfService.objects.all()],
            ).get_options(),
        },
        'chart-services-pie': {
            'options': SimplePie(
                series=[
                    OrderOfService.objects.filter(date__year=year, type_of_service=t.pk, finished=True).count()
                    for t in TypeOfService.objects.all()
                ],
                colors=[t.contextual for t in TypeOfService.objects.all()],
                labels=[t.name for t in TypeOfService.objects.all()],
            ).get_options(),
        },
    }

    return {
        'config': config,
        'line_charts': line_charts,
        'charts': charts,
    }


def get_financial_value(year, status):
    return {
        'data': [
            float(
                sum(
                    i.value for i in Invoice.objects.filter(date__month=month, date__year=year, status=status.pk)
                )
            )
            for month in range(1, 13)
        ],
        'name': status.name
    }


def get_series_service(year, type_of_service, finished):
    return {
        'data': [
            OrderOfService.objects.filter(date__month=month, date__year=year, finished=finished,
                                          type_of_service=type_of_service.pk).count()
            for month in range(1, 13)
        ],
        'name': type_of_service.name,
    }
