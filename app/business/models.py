#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/08/2020 17:18.
import datetime

from base.models import BaseModel
from config.models import TypeOfService
from django.db import models
from django.db.models import Min, Sum, Max
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from service.models import OrderOfService


class Expedient(BaseModel):
    """
        The expedient of a portion of day

        Used like:
            name, matutine
            start_time, 09:00h
            end_time, 11:30h
    """
    name = models.CharField("nome", max_length=28)
    start_time = models.TimeField("horário de início")
    end_time = models.TimeField("horário de fim")

    def __str__(self):
        return f"{self.name} de {self.start_time} até {self.end_time} ({self.get_business_hours()} min)"

    def get_back_url(self):
        return reverse('frontend:dashboard')

    def get_absolute_url(self):
        return reverse('frontend:dashboard')

    def get_delete_url(self):
        return reverse(self.get_reverse_delete, kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse(self.get_reverse_edit, kwargs={'pk': self.pk})

    def get_business_hours(self):
        end_timedelta = datetime.timedelta(hours=self.end_time.hour, minutes=self.end_time.minute)
        start_timedelta = datetime.timedelta(hours=self.start_time.hour, minutes=self.start_time.minute)
        return (end_timedelta - start_timedelta).seconds / 60


class BusinessDay(BaseModel):
    """
        Defining one day with the businesshours, if is a work day

        To get the available hours:
            - Query all orderofservices by the self.day
            - If there is any orderofservice, get the time from typeofservice
            - Query all expedient hours for the day
            - Exclude all the time consumed by the orderofservices
            - Check if the remain time fit orderofservice
    """
    day = models.DateField("dia", default=timezone.localtime(timezone.now()),
                           help_text="Caso selecionado vários dias, deixe como está!")
    color = models.CharField("cor", default="#ffddff", max_length=7,
                             help_text="Qual a cor que você deseja como plano de fundo")
    expedient_day = models.ManyToManyField(Expedient, verbose_name="Expediente",
                                           help_text="Quais são os horários disponíveis para esse dia?")
    is_work_day = models.BooleanField("dia de trabalho", default=True, help_text="Esse dia estará trabalhando?")
    force_day_full = models.BooleanField("forçar dia cheio", default=False,
                                         help_text="Forçar para que o dia mostre como lotado!")

    def __str__(self):
        return f"Dia: {self.day} Max: {self.get_expedient_hours()} min Ocupados: {self.get_consumed_hours()} min " \
               f"Lotado: {self.get_is_full()} "

    def get_back_url(self):
        return reverse('frontend:dashboard')

    def get_absolute_url(self):
        return reverse(self.get_reverse_profile, kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse(self.get_reverse_delete, kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse(self.get_reverse_edit, kwargs={'pk': self.pk})

    def get_full_name(self):
        return f"Expediente do dia {self.day.strftime('%d/%m/%Y')}"

    def get_name_html(self):
        return "Expediente"

    def get_start_date_time(self):
        return f"{self.day} {self.expedient_day.all().aggregate(min_time=Min('start_time'))['min_time'].strftime('%H:%m')}"

    def get_end_date_time(self):
        return f"{self.day} {self.expedient_day.all().aggregate(min_time=Max('end_time'))['min_time'].strftime('%H:%m')}"

    def get_expedient_hours(self):
        return sum(e.get_business_hours() for e in self.expedient_day.all())

    def get_consumed_hours(self):
        """
        :return: quantity in minutes of time consumed by orderofservices
        """
        return OrderOfService.objects.filter(date=self.day).aggregate(hours=Sum('type_of_service__time'))['hours'] or 0

    def get_is_full(self):
        """
        :return: True, if the expedient hours minus consumed hours is less than the shortest typeofservice time
        """
        return (self.get_expedient_hours() - self.get_consumed_hours()) < \
               TypeOfService.objects.all().aggregate(min_time=Min('time'))['min_time']

    def get_dict_data(self):
        return {
            'Dia': self.day,
            'Cor': mark_safe(f"<span class='badge' style='background-color: {self.color}'>{self.color}</span>"),
            'Dia de trabalho': self.is_work_day,
            'Forçar dia lotado': self.force_day_full,
        }
