#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 29/09/2020 16:41.
from datetime import datetime

from django.utils.safestring import mark_safe
from django_tables2 import TemplateColumn, tables, Column
from frontend.icons import ICON_GIFT

from .models import Profile, RewardRetrieved


class ProfileTable(tables.Table):
    # _ = TemplateColumn(template_name='base/table/buttons.html')
    name = Column(linkify=True)

    class Meta:
        model = Profile
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['name', 'whatsapp', 'birth_date', 'total_of_points']

    @staticmethod
    def render_birth_day(value):
        today = datetime.today()
        valuec = value.strftime("%d/%m/%Y")
        if value.day == today.day and value.month == today.month:
            return mark_safe(f'{valuec}<span class="ml-1 text-primary font-weight-bold">{ICON_GIFT}</span>')
        else:
            return f'{valuec}'

    @staticmethod
    def render_total_of_points(value):
        return mark_safe(f'<span data-countup>{value}</span>')


class RewardRetrievedTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = RewardRetrieved
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['reward', 'points', 'date', 'retrieved', 'customer']
