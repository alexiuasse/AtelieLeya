#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/11/2020 08:43.
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from simple_history.models import HistoricalRecords


class Invoice(models.Model):
    # customer can be retrived from service
    order_of_service = models.OneToOneField("service.OrderOfService", verbose_name="Procedimento",
                                            on_delete=models.CASCADE, null=True, blank=True,
                                            help_text="Procedimento a qual esse lançamento pertence.")
    type_of_payment = models.ForeignKey("config.TypeOfPayment", verbose_name="Tipo de Pagamento", null=True,
                                        on_delete=models.PROTECT, help_text="Qual foi o tipo de pagamento?")
    status = models.ForeignKey("config.StatusPayment", verbose_name="Status", on_delete=models.PROTECT, null=True)
    value = models.DecimalField("Valor", max_digits=11, decimal_places=2, help_text="O valor que foi pago.")
    date = models.DateField("Data", default=now, help_text="Data do pagamento.")
    observation = models.TextField("Observação", blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return "R$ {} em {} da forma {}".format(self.value, self.date, self.type_of_payment)

    def get_full_name(self):
        return "R$ {} em {} da forma {}".format(self.value, self.date, self.type_of_payment)

    # def get_html_url(self):
    #     return f'<p>{self.title}</p><a href="{self.get_edit_url()}">edit</a>'

    def get_back_url(self):
        """
        Get the back url, retrieving the service and passing the correct url
        :return: reverse url for the profile service owner
        """
        return reverse('service:orderofservice:profile',
                       kwargs={'cpk': self.order_of_service.customer.pk, 'pk': self.order_of_service.pk})

    def get_absolute_url(self):
        return reverse('service:orderofservice:profile',
                       kwargs={'cpk': self.order_of_service.customer.pk, 'pk': self.order_of_service.pk})

    def get_delete_url(self):
        return reverse(self.get_reverse_delete, kwargs={'spk': self.order_of_service.pk, 'pk': self.pk})

    def get_edit_url(self):
        return reverse(self.get_reverse_edit, kwargs={'spk': self.order_of_service.pk, 'pk': self.pk})

    def get_success_url(self):
        return reverse('financial:invoice:success', kwargs={'pk': self.pk})

    def get_is_success(self):
        return self.status.pk == settings.STATUS_PAYMENT_SUCCESS

    def get_dict_data(self):
        return {
            'Tipo de Pagamento': self.type_of_payment if self.type_of_payment else "Nenhum",
            'Status': self.status if self.status else "Nenhum",
            'Valor': "R$ {}".format(self.value),
            'Data': self.date,
            'Observação': self.observation,
        }
