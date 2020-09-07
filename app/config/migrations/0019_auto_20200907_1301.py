#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 07/09/2020 17:37.

# Generated by Django 3.1 on 2020-09-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0018_auto_20200905_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='image',
            field=models.ImageField(blank=True, help_text='Foto representando o brinde.', null=True,
                                    upload_to='images/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='typeofservice',
            name='image',
            field=models.ImageField(blank=True, help_text='Foto representando o procedimento.', null=True,
                                    upload_to='images/', verbose_name='Foto'),
        ),
    ]