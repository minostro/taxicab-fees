# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('monthly_fee_amount', models.DecimalField(max_digits=19, decimal_places=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=155)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Taxicab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ppu', models.CharField(max_length=100)),
                ('motor_number', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('serie_number', models.CharField(max_length=100)),
                ('vin_number', models.CharField(max_length=100)),
                ('manufacture_year', models.IntegerField()),
                ('acquisition_date', models.DateField()),
                ('inscription_date', models.DateField()),
                ('internal_identifier', models.CharField(max_length=100)),
                ('taxicab_check_up_expires_at', models.DateField()),
                ('belongs_to', models.ForeignKey(related_name='belongs_to', to='mantenedor.Person')),
                ('line', models.ForeignKey(to='mantenedor.Line')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
