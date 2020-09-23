#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 23/09/2020 14:04.

from datetime import date

from base.models import BaseModel
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from frontend.icons import ICON_CALENDAR


class OrderOfService(BaseModel):
    type_of_service = models.ForeignKey("config.TypeOfService", verbose_name="Procedimento", on_delete=models.SET_NULL,
                                        null=True)
    status = models.ForeignKey("config.StatusService", verbose_name="Status", on_delete=models.PROTECT)
    finished = models.BooleanField("finalizado", default=False)
    counted = models.BooleanField("contabilizado", default=False, help_text="Procedimento já foi contabilizado?")
    confirmed = models.BooleanField("confirmado", default=False, help_text="Procedimento foi confirmado?")
    canceled = models.BooleanField("cancelado", default=False, help_text="Procedimento foi cancelado?")
    date = models.DateField("Data", default=now)
    time = models.TimeField("Hora", default=now)
    observation = models.TextField("observação", blank=True)
    customer = models.ForeignKey(User, verbose_name="Cliente", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.type_of_service} de {self.customer.profile.name}"

    def get_back_url(self):
        return self.customer.profile.get_back_url_child_admin()

    def get_absolute_url(self):
        return reverse(self.get_reverse_profile, kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_absolute_url_frontend(self):
        return reverse('service:frontend:get', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse(self.get_reverse_delete, kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_edit_url(self):
        return reverse(self.get_reverse_edit, kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    def get_new_invoice_url(self):
        return reverse('financial:invoice:create', kwargs={'spk': self.pk})

    def get_confirmed_url(self):
        return reverse('service:admin:confirm', kwargs={'pk': self.pk, 'flag': 0})

    def get_finished_url(self):
        return reverse('service:admin:finish', kwargs={'pk': self.pk, 'flag': 0})

    def get_customer_finished_url(self):
        return reverse('service:admin:finish', kwargs={'pk': self.pk, 'flag': 1})

    def get_customer_confirmed_url(self):
        return reverse('service:admin:confirm', kwargs={'pk': self.pk, 'flag': 1})

    def get_cancel_url_admin(self):
        return reverse('service:admin:cancel', kwargs={'pk': self.pk})

    def get_cancel_url_frontend(self):
        return reverse('service:frontend:cancel', kwargs={'pk': self.pk})

    def get_full_name(self):
        return f"{self.type_of_service} de {self.customer.profile.get_full_name()}"

    def get_name_html(self):
        badges = ""
        if not self.confirmed or self.is_without_invoice():
            badges += '*'
        return mark_safe(f'{self.type_of_service} {badges}')

    def get_contextual(self):
        return not self.confirmed or self.is_without_invoice()

    def get_confirmed_html(self):
        return settings.ICON_CONFIRMED if self.confirmed else settings.ICON_NOT_CONFIRMED

    def get_finished_html(self):
        return settings.ICON_FINISHED if self.finished else settings.ICON_NOT_FINISHED

    def get_date_html(self):
        return f"Hoje às {self.time} <span class='text-info'>{ICON_CALENDAR}</span>" if self.date == date.today() \
            else f"{self.date.strftime('%d/%m/%Y')} às {self.time}"

    def get_status_html(self):
        return f"<span class='badge' style='background-color: {self.status.contextual};'>{self.status}</span>"

    def get_is_success(self):
        return self.status.pk == settings.STATUS_SERVICE_FINISHED

    def get_contextual_html(self):
        if self.finished:
            text = "<span class='font-weight-bold text-success'>Finalizado</span>"
        elif self.canceled:
            text = "<span class='font-weight-bold text-danger'>Cancelado</span>"
        elif not self.confirmed:
            text = "<span class='font-weight-bold text-warning'>Não Confirmado</span>"
        elif self.confirmed:
            text = "<span class='font-weight-bold text-info'>Confirmado</span>"
        else:
            text = "<span class='font-weight-bold text-default'>Em Aguardo</span>"
        return mark_safe(text)

    def get_contextual_html_admin(self):
        text = ""
        if self.canceled:
            text = "<span class='font-weight-bold text-danger'>Cancelado</span>"
        elif self.is_invoice_not_completed() or self.is_past_date_invoice():
            text = "<span class='font-weight-bold text-warning'>Fatura</span>"
        return mark_safe(text)

    def get_dict_data(self):
        return {
            'Whatsapp': self.customer.profile.whatsapp,
            'Cancelado': "Sim" if self.canceled else "Não",
            'Confirmado': mark_safe(self.get_confirmed_html),
            'Data e Hora': mark_safe(self.get_date_html()),
            'Tipo de Procedimento': mark_safe(self.type_of_service.to_html),
            'Status': mark_safe(self.get_status_html()),
            'Tempo': f'{self.type_of_service.time} min',
            # 'Finalizado': mark_safe(self.get_finished_html()),
            'Contabilizado os Pontos': "Sim" if self.counted else "Não",
            'Observação': self.observation,
        }

    # def get_invoice_sorted_by_date(self):
    #     retDict = {}
    #     for s in self.invoice_set.all().order_by('-date', '-id'):
    #         m_y = "{}/{}".format(s.date.month, s.date.year)
    #         if m_y in retDict:
    #             retDict[m_y]['invoices'].append(s)
    #         else:
    #             retDict[m_y] = {}
    #             retDict[m_y]['invoices'] = []
    #             retDict[m_y]['invoices'].append(s)
    #     return retDict

    def is_invoice_not_completed(self):
        return self.invoice.type_of_payment is None

    def is_without_invoice(self):
        return self.invoice is None

    def is_past_date_invoice(self):
        return self.invoice.date < date.today() and self.invoice.status.pk != settings.STATUS_PAYMENT_SUCCESS

    # def get_invoice_not_completed(self):
    #     if self.date < date.today():
    #         for i in self.invoice_set.all():
    #             if not i.type_of_payment:
    #                 return True
    #     return False
