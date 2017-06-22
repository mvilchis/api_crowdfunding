# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0004_auto_20170622_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingRecompensas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Proyecto', models.IntegerField()),
                ('ID_Usuario', models.IntegerField()),
                ('Monto_Recaudado', models.FloatField()),
                ('Fecha', models.DateField()),
                ('Fondeadores', models.IntegerField()),
                ('Exito_Fondeo', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectRecompesas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Proyecto', models.IntegerField()),
                ('ID_Usuario', models.IntegerField()),
                ('Categoria', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
                ('Subcategoria', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
                ('Plazo_Dias', models.IntegerField()),
                ('Fecha_Inicio', models.DateField()),
                ('Fecha_Termino', models.DateField()),
                ('Monto_Recaudado', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRecompensas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_usuario', models.IntegerField()),
                ('Sexo', models.CharField(choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10)),
                ('AnioNacimiento', models.DateField()),
                ('Estado', models.CharField(choices=[('B.C.', 'B.C.'), ('B.C.S.', 'B.C.S.'), ('Camp.', 'Camp.'), ('Coah.', 'Coah.'), ('Col.', 'Col.'), ('Chis.', 'Chis.'), ('Chih.', 'Chih.'), ('D.F.', 'D.F.'), ('Dgo.', 'Dgo.'), ('Gto.', 'Gto.')], max_length=10)),
                ('Edad', models.IntegerField()),
                ('Codigo_Postal', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
