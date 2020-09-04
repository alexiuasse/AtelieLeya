#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 15:48.

from base.models import BaseModel
from django.db import models
from django.urls import reverse_lazy

from .enums import ContextualEnum


class BaseConfigModel(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_edit_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})


class TypeOfPayment(BaseConfigModel):
    pass


class Reward(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse brinde!")
    quantity_in_points = models.IntegerField("quantidade de pontos", default=1)
    available = models.BooleanField("Disponível", default=True)
    description = models.TextField("Descrição")
    image = models.FileField("Foto", help_text="Foto representando o brinde.", blank=True, null=True)


class TypeOfService(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse procedimento!")
    time = models.FloatField("tempo", default=30, help_text="Coloque o tempo em minutos, ex.: 1hr = 60min")
    value = models.DecimalField("Valor", max_digits=11, decimal_places=2, default=0,
                                help_text="Valor do procedimento, ele será usado para auto preenchimento de alguns "
                                          "campos!")
    rewarded_points = models.IntegerField("pontos ganhos", default=0)


class StatusService(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse status")


class StatusPayment(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse status")
