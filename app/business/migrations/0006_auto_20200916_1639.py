#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 16:51.

# Generated by Django 3.1 on 2020-09-16 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('business', '0005_auto_20200916_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessday',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 19, 39, 38, 465032, tzinfo=utc),
                                   help_text='Caso selecionado vários dias, deixe como está!', verbose_name='dia'),
        ),
        migrations.AlterField(
            model_name='historicalbusinessday',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 19, 39, 38, 465032, tzinfo=utc),
                                   help_text='Caso selecionado vários dias, deixe como está!', verbose_name='dia'),
        ),
    ]