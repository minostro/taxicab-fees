# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=2, choices=[(b'01', b'January'), (b'02', b'February'), (b'03', b'March'), (b'04', b'April'), (b'05', b'May'), (b'06', b'June'), (b'07', b'July'), (b'08', b'August'), (b'09', b'Septembre'), (b'10', b'October'), (b'11', b'November'), (b'12', b'December')])),
                ('year', models.CharField(max_length=4)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('taxicab', models.ForeignKey(to='mantenedor.Taxicab')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=2, choices=[(b'01', b'January'), (b'02', b'February'), (b'03', b'March'), (b'04', b'April'), (b'05', b'May'), (b'06', b'June'), (b'07', b'July'), (b'08', b'August'), (b'09', b'Septembre'), (b'10', b'October'), (b'11', b'November'), (b'12', b'December')])),
                ('year', models.CharField(max_length=4)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fee', models.ForeignKey(blank=True, to='fees.Fee', null=True)),
                ('taxicab', models.ForeignKey(to='mantenedor.Taxicab')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
