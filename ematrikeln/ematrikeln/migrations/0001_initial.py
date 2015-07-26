# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funktunar',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('board', models.ForeignKey(to='ematrikeln.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('homeTown', models.ForeignKey(to='ematrikeln.Town')),
                ('key', models.ForeignKey(to='ematrikeln.Key')),
            ],
        ),
        migrations.AddField(
            model_name='funktunar',
            name='post',
            field=models.ForeignKey(to='ematrikeln.Post'),
        ),
        migrations.AddField(
            model_name='funktunar',
            name='user',
            field=models.ForeignKey(to='ematrikeln.User'),
        ),
    ]
