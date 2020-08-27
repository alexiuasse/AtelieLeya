#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 17:17.

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
        return reverse_lazy('{}:{}:view'.format(self._meta.app_label, self._meta.model_name))


class TypeOfPayment(BaseConfigModel):
    pass


class Reward(BaseConfigModel):
    quantity_in_points = models.FloatField("quantidade de pontos", default=1)


class TypeOfService(BaseConfigModel):
    contextutal = models.CharField("cor", default="#ffffff", max_length=7,
                                   help_text="Escolha uma cor para representar esse procedimento!")
    time = models.FloatField("tempo", default=30, help_text="Coloque o tempo em minutos, ex.: 1hr = 60min")
    value = models.DecimalField("Valor", max_digits=11, decimal_places=2, default=0,
                                help_text="Valor do procedimento, ele será usado para auto preenchimento de alguns "
                                          "campos!")
    rewarded_points = models.FloatField("pontos ganhos", default=0)


class StatusService(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse status")


class StatusPayment(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse status")
