# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ematrikeln', '0003_auto_20150726_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='study',
            field=models.CharField(max_length=30, default='randomSchool'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='town',
            name='name',
            field=models.CharField(max_length=30, default='loviisa'),
        ),
    ]
