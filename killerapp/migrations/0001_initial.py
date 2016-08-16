# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'?', max_length=100)),
                ('year', models.CharField(default=b'?', max_length=5)),
                ('detective', models.CharField(default=b'?', max_length=24)),
                ('location', models.CharField(default=b'?', max_length=13)),
                ('point_of_view', models.CharField(default=b'?', max_length=5)),
                ('murder_weapon', models.CharField(default=b'?', max_length=10)),
                ('victim_gender', models.CharField(default=b'?', max_length=5)),
                ('murderer_gender', models.CharField(default=b'?', max_length=5)),
                ('average_ratings', models.CharField(default=b'?', max_length=5)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
