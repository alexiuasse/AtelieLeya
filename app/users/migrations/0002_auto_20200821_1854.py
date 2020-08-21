#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 19:09.

# Generated by Django 3.1 on 2020-08-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='total_of_points',
            field=models.FloatField(default=0, verbose_name='Total de pontos'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='total_of_points_not_redeemed',
            field=models.FloatField(default=0, verbose_name='Total de pontos não resgatados'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='total_of_points_redeemed',
            field=models.FloatField(default=0, verbose_name='Total de pontos resgatados'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='whatsapp',
            field=models.CharField(max_length=16, verbose_name='whatsapp'),
        ),
    ]