# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0011_auto_20170818_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundingcapital',
            name='ExitoFondeo',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='fundingdeuda',
            name='ExitoFondeo',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='fundingdonation',
            name='ExitoFondeo',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='fundingrecompensas',
            name='ExitoFondeo',
            field=models.NullBooleanField(),
        ),
    ]