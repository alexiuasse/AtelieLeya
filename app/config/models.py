#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 16:09.

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


class Reward(BaseConfigModel):
    quantity_in_points = models.FloatField("quantidade de pontos", default=1)


class TypeOfService(BaseConfigModel):
    rewarded_points = models.FloatField("pontos ganhos", default=0)


class StatusService(BaseConfigModel):
    contextual = models.CharField("cor", choices=ContextualEnum.choices(), blank=True, max_length=20)