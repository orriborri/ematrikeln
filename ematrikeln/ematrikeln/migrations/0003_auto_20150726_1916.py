# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ematrikeln', '0002_auto_20150726_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='funktunar',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='key',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='lovisa', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='town',
            name='name',
            field=models.CharField(default='lovisa', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.CharField(default='exempel gatan 2', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='exmpl@ecmpl.fi', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(default='kalle', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='kalleson', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(default='medlem', max_length=30),
            preserve_default=False,
        ),
    ]
