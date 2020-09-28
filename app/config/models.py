#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/09/2020 14:36.
import datetime

from base.models import BaseModel
from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.safestring import mark_safe


class BaseConfigModel(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_edit_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})


class TypeOfPayment(BaseConfigModel):
    pass


class Reward(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse brinde!")
    quantity_in_points = models.IntegerField("quantidade de pontos", default=1)
    available = models.BooleanField("Disponível", default=True)
    description = models.TextField("Descrição", blank=True, help_text="Usado no site para descrever o brinde")
    image = models.ImageField("Foto", upload_to='images/', help_text="Foto representando o brinde.",
                              blank=True, null=True)


class TypeOfService(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse procedimento!")
    time = models.FloatField("tempo", default=30, help_text="Coloque o tempo em minutos, ex.: 1hr = 60min")
    value = models.DecimalField("Valor", max_digits=11, decimal_places=2, default=0,
                                help_text="Valor do procedimento, ele será usado para auto preenchimento de alguns "
                                          "campos!")
    rewarded_points = models.IntegerField("pontos ganhos", default=0)
    description = models.TextField("Descrição", blank=True, help_text="Usado no site para descrever o procedimento")
    image = models.ImageField("Foto", upload_to='images/', help_text="Foto representando o procedimento.",
                              blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.time} min"

    def to_html(self):
        return f"<a href={self.get_edit_url()}>{self.name}</a> (<span data-countup>{self.rewarded_points}</span> pts)"


class StatusService(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse status")


class StatusPayment(BaseConfigModel):
    contextual = models.CharField("cor", default="#ffffff", max_length=7,
                                  help_text="Escolha uma cor para representar esse status")


class Expedient(BaseModel):
    """
        The expedient of a portion of day

        Used like:
            name, matutine
            start_time, 09:00h
            end_time, 11:30h
    """
    name = models.CharField("nome", max_length=28)
    start_time = models.TimeField("horário de início", help_text="Primeiro horário disponível para agendar.")
    end_time = models.TimeField("horário de fim", help_text="Último horário disponível para agendar.")

    def __str__(self):
        return f"{self.name} de {self.start_time} até {self.end_time} ({self.get_business_hours()} min)"

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_edit_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})

    def get_back_url(self):
        return reverse(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_delete_url(self):
        return reverse(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    def get_html_repr(self):
        return f"{self.name} de {self.start_time} até {self.end_time}"

    def get_business_hours(self):
        end_timedelta = datetime.timedelta(hours=self.end_time.hour, minutes=self.end_time.minute)
        start_timedelta = datetime.timedelta(hours=self.start_time.hour, minutes=self.start_time.minute)
        return (end_timedelta - start_timedelta).seconds / 60


class HomePage(BaseModel):
    first_image = models.ImageField("Primeira Imagem", upload_to='homepage/',
                                    help_text="Imagem que fica no início da página.",
                                    blank=True, null=True)
    first_video_url = models.CharField("Primeiro Video", max_length=255,
                                       help_text="URL do primeiro vídeo, fica no início da página",
                                       blank=True, null=True)
    second_image = models.ImageField("Segunda Imagem", upload_to='homepage/',
                                     help_text="Imagem que fica na parte sobre como plano de fundo do video.",
                                     blank=True, null=True)
    second_video_url = models.CharField("Segundo Video", max_length=255,
                                        help_text="URL do segundo vídeo, fica na primeira página de sobre",
                                        blank=True, null=True)
    address = models.CharField("Endereço Completo", max_length=255,
                               help_text="Sugestão: Rua, Número, Cidade - Estado, CEP")
    whatsapp = models.CharField("Whatsapp", max_length=16, help_text="Número para contato.")
    email = models.EmailField("E-mail", help_text="Opcional!", blank=True, null=True)

    def __str__(self):
        return f"{self.address} {self.whatsapp}"

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_edit_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})

    def get_dict_data(self):
        return {
            'Endereço': self.address,
            'Whatsapp': self.whatsapp,
            'E-mail': self.email if self.email else "Nenhum",
            'Primeira Imagem': mark_safe(
                f'<a href="{self.first_image.url}" target="_blank">{self.first_image}</a>'),
            'Primeiro Video': mark_safe(
                f'<a href="{self.first_video_url}" target="_blank">{self.first_video_url}</a>'),
            'Segunda Imagem': mark_safe(
                f'<a href="{self.second_image.url}" target="_blank">{self.second_image}</a>'),
            'Segundo Video': mark_safe(
                f'<a href="{self.second_video_url}" target="_blank">{self.second_video_url}</a>'),
        }
