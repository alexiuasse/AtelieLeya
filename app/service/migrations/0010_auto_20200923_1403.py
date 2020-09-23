#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 23/09/2020 14:05.

# Generated by Django 3.1 on 2020-09-23 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0009_auto_20200923_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 17, 3, 49, 758130, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 23, 17, 3, 49, 758188, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 17, 3, 49, 758130, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 23, 17, 3, 49, 758188, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
    ]