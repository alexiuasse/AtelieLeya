#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/09/2020 13:54.
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from config.models import StatusService, StatusPayment, TypeOfPayment, Expedient

from datetime import time


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        if StatusService.objects.count() == 0:
            StatusService(name="Aguardando Confirmação", contextual="#1540ad").save()
            StatusService(name="Finalizado", contextual="#32a852").save()
            self.stdout.write(self.style.SUCCESS('Criação de status de serviço foi um sucesso!'))
        if StatusPayment.objects.count() == 0:
            StatusPayment(name="Aguardando Pagamento", contextual="#1540ad").save()
            StatusPayment(name="Finalizado", contextual="#32a852").save()
            self.stdout.write(self.style.SUCCESS('Criação de status de pagamento foi um sucesso!'))
        if TypeOfPayment.objects.count() == 0:
            TypeOfPayment(name="Dinheiro").save()
            TypeOfPayment(name="Cartão Crédito").save()
            TypeOfPayment(name="Cartão Débito").save()
            self.stdout.write(self.style.SUCCESS('Criação de tipo de pagamento foi um sucesso!'))
        if Expedient.objects.count() == 0:
            Expedient(name="Matutino", start_time=time(hour=9, minute=0), end_time=time(hour=11, minute=0)).save()
            Expedient(name="Vespertino", start_time=time(hour=13, minute=0), end_time=time(hour=18, minute=0)).save()
            self.stdout.write(self.style.SUCCESS('Criação de expediente foi um sucesso!'))
        try:
            user = User.objects.create_user('admin', password='admin123')
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Criação de admin foi um sucesso!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Criação de usuário admin falhou! Motivo %s' % e))
