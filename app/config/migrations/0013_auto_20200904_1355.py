#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:20.

# Generated by Django 3.1 on 2020-09-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0012_auto_20200904_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreward',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Disponível'),
        ),
        migrations.AddField(
            model_name='reward',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Disponível'),
        ),
    ]