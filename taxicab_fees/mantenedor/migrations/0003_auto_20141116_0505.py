# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0002_auto_20141115_2044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='line',
            options={'verbose_name': 'line', 'verbose_name_plural': 'lines'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'people'},
        ),
        migrations.AlterModelOptions(
            name='taxicab',
            options={'verbose_name': 'taxiscab', 'verbose_name_plural': 'taxicabs'},
        ),
        migrations.RemoveField(
            model_name='taxicab',
            name='vin_number',
        ),
        migrations.AlterField(
            model_name='line',
            name='monthly_fee_amount',
            field=models.DecimalField(verbose_name='monthly fee amount', max_digits=19, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='line',
            name='number',
            field=models.IntegerField(verbose_name='number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=155, verbose_name='name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_id',
            field=models.CharField(max_length=150, verbose_name='personal id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='surname'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='chassis_number',
            field=models.CharField(max_length=100, verbose_name='chasis number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='check_up_expires_at',
            field=models.DateField(verbose_name='check up expires at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='inscription_date',
            field=models.DateField(verbose_name='inscription date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='internal_identifier',
            field=models.CharField(max_length=100, verbose_name='internal identifier'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='motor_number',
            field=models.CharField(max_length=100, verbose_name='motor number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='ppu',
            field=models.CharField(max_length=100, verbose_name='ppu'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='serie_number',
            field=models.CharField(max_length=100, verbose_name='serie number'),
            preserve_default=True,
        ),
    ]
