# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjId', models.IntegerField()),
                ('ProjName', models.CharField(max_length=250)),
                ('ProjOwner', models.IntegerField()),
                ('objsType', models.IntegerField()),
                ('whatLookAt', models.IntegerField()),
                ('adAccId', models.IntegerField()),
                ('adClientId', models.IntegerField()),
                ('targetGroupId', models.IntegerField()),
                ('Token', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
            ],
        ),
    ]
