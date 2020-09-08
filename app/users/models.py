#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/09/2020 14:05.

from datetime import datetime

# users/models.py
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


class RewardRetrieved(BaseModel):
    reward = models.ForeignKey("config.Reward", on_delete=models.PROTECT, verbose_name="Brinde")
    points = models.IntegerField("Pontos", default=0)
    quantity = models.IntegerField("Quantidade", default=1)
    date = models.DateField("Data", default=timezone.localtime(timezone.now()))
    retrieved = models.BooleanField("Resgatado", default=False, help_text="Esse brinde já foi resgatado?")
    customer = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, verbose_name="Cliente")

    def __str__(self):
        return f"{self.reward} de {self.customer}"

    @property
    def get_absolute_url(self):
        return reverse('users:customuser:profile_admin', kwargs={'pk': self.customer.pk})

    @property
    def get_delete_url(self):
        return reverse('users:rewardretrieved:delete', kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('users:rewardretrieved:edit', kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    @property
    def get_back_url(self):
        return reverse('users:customuser:profile_admin', kwargs={'pk': self.customer.pk})


class CustomUser(AbstractUser):
    birth_day = models.DateField('data de nascimento', blank=True, null=True)
    whatsapp = models.CharField('whatsapp', max_length=16)
    total_of_points = models.IntegerField(default=0, verbose_name='Total de pontos')

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_new_service_url(self):
        return reverse('service:orderofservice:create', kwargs={'cpk': self.pk})

    @property
    def get_new_service_url_frontend(self):
        return reverse('service:orderofservice:create_frontend')

    @property
    def get_new_reward_url(self):
        return reverse('users:rewardretrieved:create', kwargs={'cpk': self.pk})

    def get_absolute_url(self):
        return reverse('users:customuser:profile_admin', kwargs={'pk': self.pk})

    @property
    def get_delete_url(self):
        return reverse('users:customuser:delete', kwargs={'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('users:customuser:edit', kwargs={'pk': self.pk})

    @property
    def get_edit_url_frontend(self):
        return reverse('users:customuser:edit_frontend')

    @property
    def get_calendar_url_frontend(self):
        return reverse('users:calendarfrontend:calendar_frontend')

    @property
    def get_back_url(self):
        return reverse('users:customuser:view')

    def is_birthday(self):
        today = datetime.today()
        return self.birth_day.day == today.day and self.birth_day.month == today.month if self.birth_day else False

    def get_age(self):
        return datetime.today().year - self.birth_day.year

    def get_birth_day_data(self):
        return {
            'Nome': self.get_full_name(),
            'Whatsapp': self.whatsapp,
        }

    def get_dict_data(self):
        return {
            'Usuário': self.username,
            'Nome': self.get_full_name(),
            'Whatsapp': self.whatsapp,
            'Data de Nascimento': self.birth_day,
            'E-mail': self.email,
        }

    def get_dict_data_points(self):
        return {
            'Total de Pontos': self.total_of_points,
            # 'Total de Pontos Resgatados': self.total_of_points_redeemed,
            # 'Total de Pontos Não Resgatados': self.total_of_points_not_redeemed,
        }

    def get_service_sorted_by_entry_date(self):
        retDict = {}
        for s in self.orderofservice_set.all().order_by('-date', '-id'):
            m_y = "{}/{}".format(s.date.month, s.date.year)
            if m_y in retDict:
                retDict[m_y]['services'].append(s)
            else:
                retDict[m_y] = {}
                retDict[m_y]['services'] = []
                retDict[m_y]['services'].append(s)
        # print(retDict)
        return retDict

    def get_service_sorted_by_actual_month(self):
        retDict = {}
        for s in self.orderofservice_set.filter(date__month=datetime.today().month).order_by('-date', '-id'):
            m_y = "{}/{}".format(s.date.month, s.date.year)
            if m_y in retDict:
                retDict[m_y]['services'].append(s)
            else:
                retDict[m_y] = {}
                retDict[m_y]['services'] = []
                retDict[m_y]['services'].append(s)
        # print(retDict)
        return retDict

    @property
    def sorted_reward_set(self):
        return self.rewardretrieved_set.order_by('-date', '-id')[:5]
