# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 17:36
from __future__ import unicode_literals
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('api_core', '0013_auto_20170818_0051'),
    ]
    operations = [
        migrations.AlterField(
            model_name='projectcapital',
            name='Categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]