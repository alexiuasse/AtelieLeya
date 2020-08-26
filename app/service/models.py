#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 26/08/2020 13:07.

from datetime import date

from base.models import BaseModel
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from frontend.icons import ICON_TRIANGLE_ALERT, ICON_CHECK, ICON_DOUBLE_CHECK, ICON_CALENDAR


class OrderOfService(BaseModel):
    type_of_service = models.ForeignKey("config.TypeOfService", verbose_name="Procedimento", on_delete=models.SET_NULL,
                                        null=True)
    status = models.ForeignKey("config.StatusService", verbose_name="Status", on_delete=models.PROTECT)
    finished = models.BooleanField("finalizado", default=False)
    counted = models.BooleanField("contabilizado", default=False, help_text="Procedimento já foi contabilizado?")
    confirmed = models.BooleanField("confirmado", default=False, help_text="Procedimento foi confirmado?")
    date = models.DateField("Data", default=timezone.localtime(timezone.now()))
    time = models.TimeField("Hora", default=timezone.localtime(timezone.now()))
    observation = models.TextField("observação", blank=True)
    customer = models.ForeignKey("users.CustomUser", verbose_name="Cliente", on_delete=models.CASCADE, blank=True,
                                 null=True)

    def __str__(self):
        return "{} de {}".format(self.type_of_service, self.customer.first_name)

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
        return reverse('service:orderofservice:confirmed', kwargs={'pk': self.pk, 'flag': 0})

    def get_finished_url(self):
        return reverse('service:orderofservice:finished', kwargs={'pk': self.pk, 'flag': 0})

    def get_customer_finished_url(self):
        return reverse('service:orderofservice:finished', kwargs={'pk': self.pk, 'flag': 1})

    def get_customer_confirmed_url(self):
        return reverse('service:orderofservice:confirmed', kwargs={'pk': self.pk, 'flag': 1})

    def get_full_name(self):
        return "{}".format(self.type_of_service)

    def get_name_html(self):
        badges = ""
        if not self.confirmed:
            badges += '*'
        return mark_safe(f'{self.type_of_service} {badges}')

    # maybe change to icon for better visualization
    def get_confirmed_html(self):
        return settings.ICON_CONFIRMED if self.confirmed else settings.ICON_NOT_CONFIRMED

    def get_finished_html(self):
        return settings.ICON_FINISHED if self.finished else settings.ICON_NOT_FINISHED

    def get_date_html(self):
        return "Hoje às {} <span class='text-info'>{}</span>".format(self.time,
                                                                     ICON_CALENDAR) if self.date == date.today() \
            else "{} às {}".format(self.date.strftime("%d/%m/%Y"), self.time)

    def get_status_html(self):
        return f"<span class='badge bg-{self.status.contextual}'>{self.status}</span>"

    def get_is_success(self):
        return self.status.pk == settings.STATUS_SERVICE_FINISHED

    def get_dict_data(self):
        return {
            'Confirmado': mark_safe(self.get_confirmed_html),
            'Data e Hora': mark_safe(self.get_date_html()),
            'Tipo de Procedimento': "{} ({} pts)".format(self.type_of_service, self.type_of_service.rewarded_points),
            'Status': mark_safe(self.get_status_html()),
            # 'Finalizado': mark_safe(self.get_finished_html()),
            'Contabilizado os Pontos': "Sim" if self.counted else "Não",
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
