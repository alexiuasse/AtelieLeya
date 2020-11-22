#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/11/2020 09:18.
import datetime

from config.models import TypeOfService
from django.conf import settings
from django.db import models
from django.db.models import Min, Sum, Max
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from service.models import OrderOfService
from simple_history.models import HistoricalRecords


class BusinessDay(models.Model):
    """
        Defining one day with the businesshours, if is a work day

        To get the available hours:
            - Query all orderofservices by the self.day
            - If there is any orderofservice, get the time from typeofservice
            - Query all expedient hours for the day
            - Exclude all the time consumed by the orderofservices
            - Check if the remain time fit orderofservice
    """
    day = models.DateField("dia", default=now,
                           help_text="Caso selecionado vários dias, deixe como está!")
    color = models.CharField("cor", default="#D40CD4", max_length=7,
                             help_text="Qual a cor que você deseja como plano de fundo")
    expedient_day = models.ManyToManyField("config.Expedient", verbose_name="Expediente",
                                           help_text="Quais são os horários disponíveis para esse dia?")
    is_work_day = models.BooleanField("dia de trabalho", default=True, help_text="Esse dia estará trabalhando?")
    force_day_full = models.BooleanField("forçar dia cheio", default=False,
                                         help_text="Forçar para que o dia mostre como lotado!")
    history = HistoricalRecords()

    def __str__(self):
        return f"Dia: {self.day} Max: {self.get_expedient_hours()} min Ocupados: {self.get_consumed_hours()} min " \
               f"Lotado: {self.get_is_full()} "

    @staticmethod
    def get_back_url():
        return reverse_lazy('business:admin:calendar')

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:profile', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})

    def get_full_name(self):
        return f"Expediente do dia {self.day.strftime('%d/%m/%Y')}"

    def get_name_html(self):
        return f"Exp. - {self.get_start_time()} até {self.get_end_time()}"

    def get_start_time(self):
        return self.expedient_day.all().aggregate(min_time=Min('start_time'))['min_time'].strftime('%H:%M')

    def get_end_time(self):
        return self.expedient_day.all().aggregate(max_time=Max('end_time'))['max_time'].strftime('%H:%M')

    def get_start_date_time(self):
        return f"{self.day} {self.get_start_time()}"

    def get_end_date_time(self):
        return f"{self.day} {self.get_end_time()}"

    def get_expedient_hours(self):
        return sum(e.get_business_hours() for e in self.expedient_day.all())

    def get_consumed_hours(self):
        """
        :return: quantity in minutes of time consumed by orderofservices
        """
        return OrderOfService.objects.filter(date=self.day, canceled=False) \
                   .aggregate(hours=Sum('type_of_service__time'))['hours'] or 0

    def get_remain_hours(self):
        return self.get_expedient_hours() - self.get_consumed_hours()

    def get_is_full(self):
        """
        :return: True, if the expedient hours minus consumed hours is less than the shortest typeofservice time
        """
        min_time = TypeOfService.objects.all().aggregate(min_time=Min('time'))['min_time']
        min_time = min_time if min_time else 0
        return (self.get_expedient_hours() - self.get_consumed_hours()) < min_time

    @staticmethod
    def datetime_range(start, end, delta):
        """
        Creating an range of time given an delta
        :param start: the start time
        :param end: the end time
        :param delta: the step value, ex.: 30
        :return: a list of range time
        """
        current = start
        while current < end:
            yield current
            current += delta

    def get_all_hours_list(self):
        h_list = []
        for e in self.expedient_day.all():
            start = datetime.datetime.combine(self.day, e.start_time)
            end = datetime.datetime.combine(self.day, e.end_time)
            h_list.extend(self.datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME)))
        return h_list

    def get_service_times_list(self):
        """
        :return: List of order of service that is on the day of business and not Canceled
        """
        s_times_list = []
        for s in OrderOfService.objects.filter(date=self.day, canceled=False):
            s_times_list.append(s.time)  # start
            if s.type_of_service.time / settings.SLICE_OF_TIME > 1:
                start = datetime.datetime.combine(self.day, s.time)
                end = (
                        datetime.datetime.combine(self.day, s.time) +
                        datetime.timedelta(minutes=s.type_of_service.time)
                )
                for t in self.datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME)):
                    s_times_list.append(t.time())
        return s_times_list

    def get_remain_hours_list(self):
        h_list = []
        ret_list = []
        s_times_list = self.get_service_times_list()
        for e in self.expedient_day.all():
            start = datetime.datetime.combine(self.day, e.start_time)
            end = datetime.datetime.combine(self.day, e.end_time)
            h_list.extend(self.datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME)))
        for h in h_list:
            if h.time() not in s_times_list:
                ret_list.append(h)
        return ret_list

    def get_tuple_remain_hours(self):
        """
        :return: All the remain hours separated by 30 min and excluded the hours with services
        """
        hours_tupple = []
        for h in self.get_remain_hours_list():
            hours_tupple.append((h.strftime('%H:%M'), h.strftime('%H:%M')))
        return hours_tupple

    def get_tupple_hours(self):
        h_all = self.get_all_hours_list()
        h_remain = self.get_remain_hours_list()
        h_tupple = []
        for h in h_all:
            if h in h_remain:
                h_tupple.append((h, mark_safe('<span class="text-success">Livre</span>')))
            else:
                h_tupple.append((h, mark_safe('<span class="text-danger">Ocupado</span>')))
        return h_tupple

    def get_dict_data(self):
        return {
            'Dia': self.day,
            'Cor': mark_safe(f"<span class='badge' style='background-color: {self.color}'>{self.color}</span>"),
            # 'Funcionários': self.workers,
            'Dia de trabalho': 'Sim' if self.is_work_day else 'Não',
            'Forçar dia lotado': 'Sim' if self.force_day_full else 'Não',
            'Tempo Disponível': f'{self.get_remain_hours()} min',
        }
