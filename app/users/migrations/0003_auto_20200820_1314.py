#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 20/08/2020 14:39.

# Generated by Django 3.1 on 2020-08-20 16:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20200819_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='birthday',
            new_name='birth_day',
        ),
    ]
