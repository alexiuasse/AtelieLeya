#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:20.

# Generated by Django 3.1 on 2020-09-04 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0020_auto_20200904_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 14, 25, 56, 946728, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 4, 14, 25, 56, 946853, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 14, 25, 56, 946728, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 4, 14, 25, 56, 946853, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
    ]