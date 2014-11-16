# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personal_id',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='surname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
