#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 16:51.

# Generated by Django 3.1 on 2020-09-16 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_auto_20200916_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 19, 39, 38, 439616, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='rewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 19, 39, 38, 439616, tzinfo=utc),
                                   verbose_name='Data'),
        ),
    ]