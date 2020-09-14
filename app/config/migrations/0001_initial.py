#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/09/2020 13:05.

# Generated by Django 3.1 on 2020-09-14 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expedient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28, verbose_name='nome')),
                ('start_time', models.TimeField(verbose_name='horário de início')),
                ('end_time', models.TimeField(verbose_name='horário de fim')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse brinde!',
                                  max_length=7, verbose_name='cor')),
                ('quantity_in_points', models.IntegerField(default=1, verbose_name='quantidade de pontos')),
                ('available', models.BooleanField(default=True, verbose_name='Disponível')),
                ('description', models.TextField(blank=True, help_text='Usado no site para descrever o brinde',
                                                 verbose_name='Descrição')),
                ('image',
                 models.ImageField(blank=True, help_text='Foto representando o brinde.', null=True, upload_to='images/',
                                   verbose_name='Foto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse status',
                                  max_length=7, verbose_name='cor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse status',
                                  max_length=7, verbose_name='cor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeOfPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeOfService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse procedimento!',
                                  max_length=7, verbose_name='cor')),
                ('time', models.FloatField(default=30, help_text='Coloque o tempo em minutos, ex.: 1hr = 60min',
                                           verbose_name='tempo')),
                ('value', models.DecimalField(decimal_places=2, default=0,
                                              help_text='Valor do procedimento, ele será usado para auto preenchimento de alguns campos!',
                                              max_digits=11, verbose_name='Valor')),
                ('rewarded_points', models.IntegerField(default=0, verbose_name='pontos ganhos')),
                ('description', models.TextField(blank=True, help_text='Usado no site para descrever o procedimento',
                                                 verbose_name='Descrição')),
                ('image', models.ImageField(blank=True, help_text='Foto representando o procedimento.', null=True,
                                            upload_to='images/', verbose_name='Foto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalTypeOfService',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse procedimento!',
                                  max_length=7, verbose_name='cor')),
                ('time', models.FloatField(default=30, help_text='Coloque o tempo em minutos, ex.: 1hr = 60min',
                                           verbose_name='tempo')),
                ('value', models.DecimalField(decimal_places=2, default=0,
                                              help_text='Valor do procedimento, ele será usado para auto preenchimento de alguns campos!',
                                              max_digits=11, verbose_name='Valor')),
                ('rewarded_points', models.IntegerField(default=0, verbose_name='pontos ganhos')),
                ('description', models.TextField(blank=True, help_text='Usado no site para descrever o procedimento',
                                                 verbose_name='Descrição')),
                ('image',
                 models.TextField(blank=True, help_text='Foto representando o procedimento.', max_length=100, null=True,
                                  verbose_name='Foto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical type of service',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTypeOfPayment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical type of payment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalStatusService',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse status',
                                  max_length=7, verbose_name='cor')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical status service',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalStatusPayment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse status',
                                  max_length=7, verbose_name='cor')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical status payment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReward',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('contextual',
                 models.CharField(default='#ffffff', help_text='Escolha uma cor para representar esse brinde!',
                                  max_length=7, verbose_name='cor')),
                ('quantity_in_points', models.IntegerField(default=1, verbose_name='quantidade de pontos')),
                ('available', models.BooleanField(default=True, verbose_name='Disponível')),
                ('description', models.TextField(blank=True, help_text='Usado no site para descrever o brinde',
                                                 verbose_name='Descrição')),
                ('image',
                 models.TextField(blank=True, help_text='Foto representando o brinde.', max_length=100, null=True,
                                  verbose_name='Foto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical reward',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalExpedient',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=28, verbose_name='nome')),
                ('start_time', models.TimeField(verbose_name='horário de início')),
                ('end_time', models.TimeField(verbose_name='horário de fim')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical expedient',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
