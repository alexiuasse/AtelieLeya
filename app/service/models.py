#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/08/2020 11:25.

from datetime import datetime

from base.models import BaseModel
from django.db import models


class OrderOfService(BaseModel):
    type_of_service = models.ForeignKey("config.TypeOfService", verbose_name="Procedimento", on_delete=models.SET_NULL,
                                        null=True)
    status = models.ForeignKey("config.StatusService", verbose_name="Status", on_delete=models.PROTECT)
    finished = models.BooleanField("finalizado", default=False,
                                   help_text="Marque apenas quando procedimento finalizado")
    counted = models.BooleanField("contabilizado", default=False, help_text="Procedimento já foi contabilizado?")
    date_time = models.DateTimeField("Data e Hora", default=datetime.now)
    observation = models.TextField("observação", blank=True)

    def __str__(self):
        return "{} às {}, status: {}".format(self.type_of_service, self.date_time, self.status)

    def get_customer_name(self):
        return self.customuser_set.all().first().first_name

    def get_html_url(self):
        return f'<p>{self.title}</p><a href="{self.get_edit_url()}">edit</a>'
