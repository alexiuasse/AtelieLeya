#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 18:08.

from datetime import date

from base.models import BaseModel
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from frontend.icons import ICON_TRIANGLE_ALERT, ICON_CHECK, ICON_DOUBLE_CHECK, ICON_CALENDAR


class OrderOfService(BaseModel):
    type_of_service = models.ForeignKey("config.TypeOfService", verbose_name="Procedimento", on_delete=models.SET_NULL,
                                        null=True)
    status = models.ForeignKey("config.StatusService", verbose_name="Status", on_delete=models.PROTECT)
    finished = models.BooleanField("finalizado", default=False,
                                   help_text="Marque apenas quando procedimento finalizado")
    counted = models.BooleanField("contabilizado", default=False, help_text="Procedimento já foi contabilizado?")
    confirmed = models.BooleanField("confirmado", default=False, help_text="Procedimento foi confirmado?")
    date = models.DateField("Data", default=now)
    time = models.TimeField("Hora", default=now)
    observation = models.TextField("observação", blank=True)
    customer = models.ForeignKey("users.CustomUser", verbose_name="Cliente", on_delete=models.CASCADE, blank=True,
                                 null=True)

    def __str__(self):
        return "{} de {}".format(self.type_of_service, self.customer.first_name)

    def get_full_name(self):
        return "{}".format(self.type_of_service)

    def get_html_url(self):
        return f'<p>{self.title}</p><a href="{self.get_edit_url()}">edit</a>'

    def get_back_url(self):
        """
        Get the back url, retrieving the customer and passing the correct url
        :return: reverse url for the profile customer owner
        """
        return reverse('users:customuser:profile', kwargs={'pk': self.customer.pk})

    def get_absolute_url(self):
        return reverse(self.get_reverse_profile, kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_delete_url(self):
        return reverse(self.get_reverse_delete, kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_edit_url(self):
        return reverse(self.get_reverse_edit, kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_new_invoice_url(self):
        return reverse('financial:invoice:create', kwargs={'spk': self.pk})

    def get_confirmed_url(self):
        return reverse('service:orderofservice:confirmed', kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_finished_url(self):
        return reverse('service:orderofservice:finished', kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    # maybe change to icon for better visualization
    def get_confirmed_html(self):
        return f"Sim <span class='text-success'>{ICON_CHECK}</span>" if self.confirmed else \
            f"Não <span class='text-danger'>{ICON_TRIANGLE_ALERT}</span>"

    def get_finished_html(self):
        return f"Sim <span class='text-success'>{ICON_DOUBLE_CHECK}</span>" if self.finished else \
            f"Não <span class='text-primary'>{ICON_TRIANGLE_ALERT}</span>"

    def get_date_html(self):
        return "Hoje às {} <span class='text-info'>{}</span>".format(self.time,
                                                                     ICON_CALENDAR) if self.date == date.today() \
            else "{} às {}".format(self.date.strftime("%d/%m/%Y"), self.time)

    def get_dict_data(self):
        return {
            'Confirmado': "Sim" if self.confirmed else "Não",
            'Data e Hora': mark_safe(self.get_date_html()),
            'Tipo de Procedimento': "{} ({} pts)".format(self.type_of_service, self.type_of_service.rewarded_points),
            # 'Status': self.status,
            'Finalizado': mark_safe(self.get_finished_html()),
            'Contabilizado os Pontos': mark_safe(self.get_confirmed_html()),
            'Observação': self.observation,
        }

    def get_invoice_sorted_by_date(self):
        retDict = {}
        for s in self.invoice_set.all().order_by('-date', '-id'):
            m_y = "{}/{}".format(s.date.month, s.date.year)
            if m_y in retDict:
                retDict[m_y]['invoices'].append(s)
            else:
                retDict[m_y] = {}
                retDict[m_y]['invoices'] = []
                retDict[m_y]['invoices'].append(s)
        return retDict

    def get_past_date_without_invoice(self):
        return self.date < date.today() and self.invoice_set.all().count() == 0
