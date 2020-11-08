#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 10:43.

from django.db import models
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


# class Testimonials(models.Model):
#     title = models.CharField(_('Title'), max_length=128, default='')
#     subtitle = models.CharField(_('Subtitle'), max_length=128, default='')
#     image = models.ImageField(_('Image'), upload_to='images/testimonials/')
#     testimonial = models.TextField(_('Testimonial'))
#     show = models.BooleanField(_('Show in website?'), default=True)
#     history = HistoricalRecords()
#
#     def get_absolute_url(self):
#         return reverse_lazy('homepage:homepage:view')
#
#     def get_edit_url(self):
#         return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})
#
#     def get_delete_url(self):
#         return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})
#
#
# class ClientsImage(models.Model):
#     name = models.CharField(_('Name'), max_length=128)
#     image = models.ImageField(_('Image'), upload_to='images/clients/')
#     show = models.BooleanField(_('Show in website?'), default=True)
#     history = HistoricalRecords()
#
#     def get_absolute_url(self):
#         return reverse_lazy('homepage:homepage:view')
#
#     def get_edit_url(self):
#         return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})
#
#     def get_delete_url(self):
#         return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})


class HomePage(models.Model):
    title = models.CharField("Título", max_length=128)
    subtitle = models.CharField("Subtítulo", max_length=128)
    address = models.CharField("Endereço Completo", max_length=255,
                               help_text="Sugestão: Rua, Número, Cidade - Estado, CEP")
    first_image = models.ImageField("Primeira Imagem", upload_to='homepage/background/',
                                    help_text="Plano de fundo da primeira página.",
                                    blank=True, null=True)
    first_video_url = models.CharField("Primeiro Video", max_length=255,
                                       help_text="URL do primeiro vídeo, fica no início da página",
                                       blank=True, null=True)
    second_image = models.ImageField("Segunda Imagem", upload_to='homepage/background/',
                                     help_text="Plano de fundo da página sobre.",
                                     blank=True, null=True)
    second_video_url = models.CharField("Segundo Video", max_length=255,
                                        help_text="URL do segundo vídeo, fica na primeira página de sobre",
                                        blank=True, null=True)
    whatsapp = models.CharField("Whatsapp", max_length=16, help_text="Número do whatsapp")
    whatsapp_link = models.CharField("Link para whatsapp", max_length=256, help_text="Link direcionando para whatsapp",
                                     default='https://www.google.com')
    instagram = models.CharField("Instagram", max_length=256, help_text="Link direcionando para instagram",
                                 default='https://www.google.com')
    facebook = models.CharField("Facebook", max_length=256, help_text="Link direcionando para facebook",
                                default='https://www.google.com')
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.address} {self.whatsapp}"

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_edit_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:edit', kwargs={'pk': self.pk})

    def get_dict_data(self):
        return {
            "Título": self.title,
            "Subtítulo": self.subtitle,
            "Whatsapp": self.whatsapp,
            "Link para whatsapp": self.whatsapp_link,
            "Instagram": self.instagram,
            "Facebook": self.facebook,
            "Primeira Imagem": mark_safe(
                f'<a href="{self.first_image.url}" target="_blank">{self.first_image}</a>') if self.first_image else "",
            'Primeiro Video': mark_safe(
                f'<a href="{self.first_video_url}" target="_blank">{self.first_video_url}</a>'),
            "Segunda Imagem": mark_safe(
                f'<a href="{self.second_image.url}" target="_blank">{self.second_image}</a>') if self.second_image else "",
            'Segundo Video': mark_safe(
                f'<a href="{self.second_video_url}" target="_blank">{self.second_video_url}</a>'),
        }
