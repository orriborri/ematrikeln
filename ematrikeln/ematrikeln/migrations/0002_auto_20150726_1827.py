# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ematrikeln', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='homeTown',
        ),
        migrations.RemoveField(
            model_name='user',
            name='key',
        ),
    ]
