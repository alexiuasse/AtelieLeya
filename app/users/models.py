#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 01/09/2020 09:50.

# users/models.py
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    birth_day = models.DateField('data de nascimento', blank=True, null=True)
    whatsapp = models.CharField('whatsapp', max_length=16)
    total_of_points = models.FloatField(default=0, verbose_name='Total de pontos')

    # total_of_points_redeemed = models.FloatField(default=0, verbose_name='Total de pontos resgatados')
    # total_of_points_not_redeemed = models.FloatField(default=0, verbose_name='Total de pontos não resgatados')

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_new_service_url(self):
        return reverse('service:orderofservice:create', kwargs={'cpk': self.pk})

    def get_absolute_url(self):
        return reverse('users:customuser:profile', kwargs={'pk': self.pk})

    @property
    def get_delete_url(self):
        return reverse('users:customuser:delete', kwargs={'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('users:customuser:edit', kwargs={'pk': self.pk})

    @property
    def get_back_url(self):
        return reverse('users:customuser:view')

    def is_birthday(self):
        today = datetime.today()
        return self.birth_day.day == today.day and self.birth_day.month == today.month

    def get_age(self):
        return datetime.today().year - self.birth_day.year

    def get_birth_day_data(self):
        return {
            'Nome': self.get_full_name(),
            'Whatsapp': self.whatsapp,
        }

    def get_dict_data(self):
        return {
            'Username': self.username,
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
