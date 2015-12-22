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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Funktunar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('year', models.IntegerField(null=True)),
                ('board', models.ForeignKey(to='ematrikeln.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Gymnasium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=30)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('study', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=10)),
                ('homeTown', models.ForeignKey(to='ematrikeln.Town')),
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
