#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/09/2020 11:47.

# Generated by Django 3.1 on 2020-09-24 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('financial', '0002_auto_20200924_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 24, 14, 42, 25, 331635, tzinfo=utc),
                                   help_text='Data do pagamento.', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 24, 14, 42, 25, 331635, tzinfo=utc),
                                   help_text='Data do pagamento.', verbose_name='Data'),
        ),
    ]
