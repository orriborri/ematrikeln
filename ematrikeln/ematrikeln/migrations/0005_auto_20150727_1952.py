# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ematrikeln', '0004_auto_20150727_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gymnasium',
            field=models.ForeignKey(to='ematrikeln.Gymnasium', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(to='ematrikeln.School', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='homeTown',
            field=models.ForeignKey(to='ematrikeln.Town', null=True),
        ),
    ]
