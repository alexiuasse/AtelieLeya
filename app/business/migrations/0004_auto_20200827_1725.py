#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 17:26.

# Generated by Django 3.1 on 2020-08-27 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('business', '0003_auto_20200827_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessday',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 20, 25, 33, 836839, tzinfo=utc),
                                   verbose_name='dia'),
        ),
        migrations.AlterField(
            model_name='historicalbusinessday',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 20, 25, 33, 836839, tzinfo=utc),
                                   verbose_name='dia'),
        ),
    ]