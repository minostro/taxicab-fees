# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fee',
            options={'verbose_name': 'fee', 'verbose_name_plural': 'fees'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
        migrations.AlterField(
            model_name='fee',
            name='amount',
            field=models.DecimalField(verbose_name='amount', max_digits=19, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fee',
            name='month',
            field=models.CharField(max_length=2, verbose_name='month', choices=[(b'01', 'January'), (b'02', 'February'), (b'03', 'March'), (b'04', 'April'), (b'05', 'May'), (b'06', 'June'), (b'07', 'July'), (b'08', 'August'), (b'09', 'September'), (b'10', 'October'), (b'11', 'November'), (b'12', 'December')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fee',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='paid'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fee',
            name='taxicab',
            field=models.ForeignKey(verbose_name='taxicab', to='mantenedor.Taxicab'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fee',
            name='year',
            field=models.CharField(max_length=4, verbose_name='year'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(verbose_name='amount', max_digits=19, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.CharField(max_length=2, verbose_name='month', choices=[(b'01', 'January'), (b'02', 'February'), (b'03', 'March'), (b'04', 'April'), (b'05', 'May'), (b'06', 'June'), (b'07', 'July'), (b'08', 'August'), (b'09', 'September'), (b'10', 'October'), (b'11', 'November'), (b'12', 'December')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='taxicab',
            field=models.ForeignKey(verbose_name='taxicab', to='mantenedor.Taxicab'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='year',
            field=models.CharField(max_length=4, verbose_name='year'),
            preserve_default=True,
        ),
    ]
