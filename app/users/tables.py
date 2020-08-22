#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/08/2020 11:05.
from datetime import datetime

from django.utils.safestring import mark_safe
from django_tables2 import TemplateColumn, tables, Column
from frontend.icons import ICON_GIFT

from .models import CustomUser


class CustomUserTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')
    name = Column(accessor='first_name', verbose_name='Nome', linkify=True)

    class Meta:
        model = CustomUser
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['name', 'username', 'whatsapp', 'birth_day']

    @staticmethod
    def render_birth_day(value):
        today = datetime.today()
        valuec = value.strftime("%d/%m/%Y")
        if value.day == today.day and value.month == today.month:
            return mark_safe(f'{valuec}<span class="ml-1 text-primary font-weight-bold">{ICON_GIFT}</span>')
        else:
            return f'{valuec}'
