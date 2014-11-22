# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0003_auto_20141116_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxicab',
            name='belongs_to',
            field=models.ForeignKey(related_name='belongs_to', verbose_name='belongs to', to='mantenedor.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxicab',
            name='line',
            field=models.ForeignKey(verbose_name='line', to='mantenedor.Line'),
            preserve_default=True,
        ),
    ]
