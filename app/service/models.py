#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 13:53.

from datetime import datetime

from base.models import BaseModel
from django.db import models
from django.urls import reverse


class OrderOfService(BaseModel):
    type_of_service = models.ForeignKey("config.TypeOfService", verbose_name="Procedimento", on_delete=models.SET_NULL,
                                        null=True)
    # status = models.ForeignKey("config.StatusService", verbose_name="Status", on_delete=models.PROTECT)
    finished = models.BooleanField("finalizado", default=False,
                                   help_text="Marque apenas quando procedimento finalizado")
    counted = models.BooleanField("contabilizado", default=False, help_text="Procedimento já foi contabilizado?")
    confirmed = models.BooleanField("confirmado", default=False, help_text="Procedimento foi confirmado?")
    date = models.DateField("Data", default=datetime.today)
    time = models.TimeField("Hora", default=datetime.now)
    observation = models.TextField("observação", blank=True)

    def __str__(self):
        return "{} de {}".format(self.type_of_service, self.get_customer_name())

    def get_full_name(self):
        return "{}".format(self.type_of_service)

    def get_customer_name(self):
        return self.customuser_set.all().first().first_name if self.customuser_set.all().first() else ""

    def get_customer_contact(self):
        return self.customuser_set.all().first().whatsapp if self.customuser_set.all().first() else ""

    def get_cpk_customer(self):
        return self.customuser_set.all().first().pk

    def get_html_url(self):
        return f'<p>{self.title}</p><a href="{self.get_edit_url()}">edit</a>'

    def get_back_url(self):
        return reverse('dashboard')

    def get_absolute_url(self):
        return reverse(self.get_reverse_profile, kwargs={'cpk': self.get_cpk_customer(), 'pk': self.pk})

    def get_delete_url(self):
        return reverse(self.get_reverse_delete, kwargs={'cpk': self.get_cpk_customer(), 'pk': self.pk})

    def get_edit_url(self):
        return reverse(self.get_reverse_edit, kwargs={'cpk': self.get_cpk_customer(), 'pk': self.pk})

    def get_confirmed_url(self):
        return reverse('service:orderofservice:confirmed', kwargs={'cpk': self.get_cpk_customer(), 'pk': self.pk})

    def get_finished_url(self):
        return reverse('service:orderofservice:finished', kwargs={'cpk': self.get_cpk_customer(), 'pk': self.pk})

    def get_dict_data(self):
        return {
            'Confirmado': "Sim" if self.confirmed else "Não",
            'Data e Hora': "{} {}".format(self.date, self.time),
            'Tipo de Procedimento': "{} ({} pts)".format(self.type_of_service, self.type_of_service.rewarded_points),
            # 'Status': self.status,
            'Finalizado': "Sim" if self.finished else "Não",
            'Contabilizado os Pontos': "Sim" if self.counted else "Não",
            'Observação': self.observation,
        }
