#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/09/2020 10:10.
from datetime import datetime

from django.utils.safestring import mark_safe
from django_tables2 import TemplateColumn, tables, Column
from frontend.icons import ICON_GIFT

from .models import Profile, RewardRetrieved


class ProfileTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')
    name = Column(linkify=True)

    class Meta:
        model = Profile
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['name', 'whatsapp', 'birth_date']

    @staticmethod
    def render_birth_day(value):
        today = datetime.today()
        valuec = value.strftime("%d/%m/%Y")
        if value.day == today.day and value.month == today.month:
            return mark_safe(f'{valuec}<span class="ml-1 text-primary font-weight-bold">{ICON_GIFT}</span>')
        else:
            return f'{valuec}'


class RewardRetrievedTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = RewardRetrieved
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['reward', 'points', 'date', 'retrieved', 'customer']
