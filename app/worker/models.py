#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 13/09/2020 12:47.

from django.db import models
from base.models import BaseModel
from django.urls import reverse


class WorkerProfile(BaseModel):
    expertise = models.ManyToManyField("config.TypeOfService", blank=True, verbose_name="Especialidades",
                                       help_text="Quais procedimentos esse funcionário é capaz de fazer?")
    customuser = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE, verbose_name="Usuário do sistema")

    def __str__(self):
        return self.customuser.first_name

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
        return self.customuser.username
