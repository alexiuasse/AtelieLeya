#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 14:01.

# Generated by Django 3.1 on 2020-08-21 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0005_auto_20200821_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Data'),
        ),
    ]
