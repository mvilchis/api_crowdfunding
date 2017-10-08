# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0014_auto_20170818_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcapital',
            name='Categoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Categoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Categoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Categoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
