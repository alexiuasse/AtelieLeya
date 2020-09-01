#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 01/09/2020 10:36.
from datetime import datetime

from config.models import TypeOfService, StatusPayment
from financial.models import Invoice
from frontend.icons import ICON_COIN, ICON_PERSON, ICON_WAND, ICON_GIFT, ICON_CALENDAR, ICON_TRIANGLE_ALERT
from service.models import OrderOfService
from users.models import CustomUser

from .apexcharts.line import Line
from .apexcharts.simple_pie import SimplePie


def context_dashboard():
    today = datetime.today()
    birthdays = CustomUser.objects.filter(birth_day__day=today.day, birth_day__month=today.month)
    services_today = OrderOfService.objects.filter(date=today)
    services_not_confirmed = OrderOfService.objects.filter(confirmed=False)
    services_invoice_not_completed = [obj for obj in OrderOfService.objects.all() if obj.get_invoice_not_completed()]
    return {
        'today': {
            'pre_title': f'Hoje {today.strftime("%d/%m/%Y")}',
            'title': {
                'text': 'O que você tem para Hoje',
                'icon': ICON_CALENDAR,
            },
        },
        'birthdays': {
            'pre_title': 'Clientes',
            'title': {
                'text': 'Aniversariantes de Hoje',
                'icon': ICON_GIFT,
            },
            'data': birthdays,
        },
        'services_today': {
            'pre_title': 'Procedimentos',
            'title': {
                'text': 'Procedimentos para Hoje',
                'icon': ICON_WAND,
            },
            'data': services_today,
        },
        'atention': {
            'pre_title': 'Atenção!',
            'title': {
                'text': 'Algumas coisas que precisam de atenção',
                'icon': ICON_TRIANGLE_ALERT
            },
        },
        'services_not_confirmed': {
            'pre_title': 'Procedimentos',
            'title': {
                'text': 'Procedimentos não confirmados',
                'icon': ICON_WAND,
            },
            'data': services_not_confirmed,
        },
        'services_invoice_not_completed': {
            'pre_title': 'Procedimentos',
            'title': {
                'text': 'Procedimentos com faturamento não completo',
                'icon': ICON_WAND,
            },
            'data': services_invoice_not_completed,
        },
    }


def context_chart(req_year):
    year = datetime.today().year if not req_year else req_year

    headers_charts_line = {
        'customers': {
            'pre_title': 'Clientes',
            'title': {
                'text': 'Ganho de Clientes',
                'icon': ICON_PERSON,
            },
            'chart_id': 'chart-customers',
            'links': {

            }
        },
        'financials': {
            'pre_title': 'Financeiro',
            'title': {
                'text': 'Rendimento Mensal',
                'icon': ICON_COIN,
            },
            'chart_id': 'chart-financial',
            'links': {

            }
        },
        'services': {
            'pre_title': 'Procedimentos',
            'title': {
                'text': 'Procedimentos',
                'icon': ICON_WAND,
            },
            'chart_id': 'chart-services',
            'links': {

            }
        },
    }

    headers_charts_pie = {
        'reward': {
            'pre_title': 'Brinde',
            'title': {
                'text': 'Brinde',
                'icon': ICON_GIFT,
            },
            'chart_id': 'chart-reward',
            'links': {

            }
        },
        'financials-pie': {
            'pre_title': 'Financeiro',
            'title': {
                'text': 'Divisão por status',
                'icon': ICON_COIN,
            },
            'chart_id': 'chart-financial-pie',
            'links': {

            }
        },
        'services-pie': {
            'pre_title': 'Procedimento',
            'title': {
                'text': 'Procedimentos',
                'icon': ICON_WAND,
            },
            'chart_id': 'chart-services-pie',
            'links': {

            }
        },
    }

    charts = {
        'chart-customers': {
            'options': Line(
                title=f'Clientes - Total ({CustomUser.objects.filter(date_joined__year=year).count()})',
                x_title='Mês',
                y_title='Quantidade',
                series=[{
                    'data': [
                        CustomUser.objects.filter(date_joined__month=month, date_joined__year=year).count()
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
                title=f'Brindes Mais Escolhidos - Total ({OrderOfService.objects.filter(date__year=year).count()})',
                series=[OrderOfService.objects.filter(date__year=year, type_of_service=t.pk).count() for t in
                        TypeOfService.objects.all()],
                colors=[t.contextual for t in TypeOfService.objects.all()],
                labels=[t.name for t in TypeOfService.objects.all()],
            ).get_options(),
        },
        # FINANCIAL
        'chart-financial': {
            'options': Line(
                title='Rendimento Mensal',
                x_title='Mês',
                y_title='Valor em R$',
                series=[get_financial_value(year, s) for s in StatusPayment.objects.all()],
                colors=[t.contextual for t in StatusPayment.objects.all()],
            ).get_options(),
        },
        'chart-financial-pie': {
            'options': SimplePie(
                title=f'Divisão Por Status - Total ({Invoice.objects.filter(date__year=year).count()})',
                series=[Invoice.objects.filter(date__year=year, status=t.pk).count() for t in
                        StatusPayment.objects.all()],
                colors=[t.contextual for t in StatusPayment.objects.all()],
                labels=[t.name for t in StatusPayment.objects.all()],
            ).get_options(),
        },
        # SERVICE
        'chart-services': {
            'options': Line(
                title=f'Procedimentos - Total ({OrderOfService.objects.filter(date__year=year).count()})',
                x_title='Mês',
                y_title='Quantidade',
                series=[get_series_service(year, t) for t in TypeOfService.objects.all()],
                colors=[t.contextual for t in TypeOfService.objects.all()],
            ).get_options(),
        },
        'chart-services-pie': {
            'options': SimplePie(
                title=f'Divisão Por Procedimento - Total ({OrderOfService.objects.filter(date__year=year).count()})',
                series=[OrderOfService.objects.filter(date__year=year, type_of_service=t.pk).count() for t in
                        TypeOfService.objects.all()],
                colors=[t.contextual for t in TypeOfService.objects.all()],
                labels=[t.name for t in TypeOfService.objects.all()],
            ).get_options(),
        },
    }

    return {
        'headers_charts_line': headers_charts_line,
        'headers_charts_pie': headers_charts_pie,
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


def get_series_service(year, type_of_service):
    return {
        'data': [
            OrderOfService.objects.filter(date__month=month, date__year=year,
                                          type_of_service=type_of_service.pk).count()
            for month in range(1, 13)
        ],
        'name': type_of_service.name,
    }
