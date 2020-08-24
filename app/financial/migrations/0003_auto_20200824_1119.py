#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 13:18.

# Generated by Django 3.1 on 2020-08-24 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('financial', '0002_auto_20200824_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoice',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Data do pagamento.',
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Data do pagamento.',
                                   verbose_name='Data'),
        ),
    ]