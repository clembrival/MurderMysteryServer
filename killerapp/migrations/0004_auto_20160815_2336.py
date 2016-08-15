# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('killerapp', '0003_auto_20160813_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='victim_gender',
            field=models.CharField(default=b'?', max_length=5),
        ),
        migrations.AlterField(
            model_name='entry',
            name='year',
            field=models.CharField(default=b'?', max_length=5),
        ),
    ]
