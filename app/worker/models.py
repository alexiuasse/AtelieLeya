#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 09:55.
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from base.models import BaseModel
from django.urls import reverse


class WorkerProfile(BaseModel):
    name = models.CharField("nome", max_length=150)
    birth_date = models.DateField('data de nascimento', blank=True, null=True, help_text="Informe uma data válida!")
    whatsapp = models.CharField('whatsapp', max_length=16, help_text="Esse será o número usado para contato!")
    expertise = models.ManyToManyField("config.TypeOfService", blank=True, verbose_name="Especialidades",
                                       help_text="Quais procedimentos esse funcionário é especializado?")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário do sistema")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('worker:workerprofile:profile', kwargs={'pk': self.pk})

    @property
    def get_delete_url(self):
        return reverse('worker:workerprofile:delete', kwargs={'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('worker:workerprofile:edit', kwargs={'pk': self.pk})

    @property
    def get_back_url(self):
        return reverse('worker:workerprofile:view')

    def get_username(self):
        return self.user.username

    def get_full_name(self):
        return self.name

    def is_birthday(self):
        today = datetime.today()
        return self.birth_date.day == today.day and self.birth_date.month == today.month if self.birth_date else False

    def get_age(self):
        return datetime.today().year - self.birth_day.year

    def get_dict_data(self):
        return {
            'Usuário': self.user.username,
            'Nome': self.get_full_name(),
            'Whatsapp': self.whatsapp,
            'Data de Nascimento': self.birth_date,
            'E-mail': self.user.email,
        }

    def has_service(self):
        return self.user.orderofservice_set.count()

    def get_service_sorted_by_entry_date(self):
        retDict = {}
        for s in self.user.orderofservice_set.all().order_by('-date', '-id'):
            m_y = "{}/{}".format(s.date.month, s.date.year)
            if m_y in retDict:
                retDict[m_y]['services'].append(s)
            else:
                retDict[m_y] = {}
                retDict[m_y]['services'] = []
                retDict[m_y]['services'].append(s)
        return retDict

    def get_service_sorted_by_actual_month(self):
        return self.user.orderofservice_set.all().order_by('-id')[:5]
