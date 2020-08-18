#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/08/2020 14:27.

from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    @property
    def get_delete_url(self):
        return reverse('{}:{}:delete'.format(self._meta.app_label, self._meta.model_name), kwargs={'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('{}:{}:edit'.format(self._meta.app_label, self._meta.model_name), kwargs={'pk': self.pk})

    @property
    def get_back_url(self):
        return reverse('{}:{}:view'.format(self._meta.app_label, self._meta.model_name))
