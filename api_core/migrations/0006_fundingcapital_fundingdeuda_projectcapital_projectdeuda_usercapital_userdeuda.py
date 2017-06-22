# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0005_fundingrecompensas_projectrecompesas_userrecompensas'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingCapital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Proyecto', models.IntegerField()),
                ('ID_Usuario', models.IntegerField()),
                ('Monto_Recaudado', models.FloatField()),
                ('Fecha', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingDeuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Proyecto', models.IntegerField()),
                ('ID_Usuario', models.IntegerField()),
                ('Monto_Recaudado', models.FloatField()),
                ('Fecha', models.DateField()),
                ('Tipo_Movimiento', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectCapital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Proyecto', models.IntegerField()),
                ('ID_Usuario', models.IntegerField()),
                ('Categoria', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
                ('Subcategoria', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
                ('Monto_Aprobado', models.FloatField()),
                ('Plazo_Meses', models.IntegerField()),
                ('Tasa_Interes', models.FloatField()),
                ('Fecha_Inicio', models.DateField()),
                ('Fecha_Termino', models.DateField()),
                ('Monto_Recaudado', models.FloatField()),
                ('Cuota_Comision', models.FloatField()),
                ('Fondeado', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectDeuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Proyecto', models.IntegerField()),
                ('ID_Usuario', models.IntegerField()),
                ('Categoria', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
                ('Subcategoria', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
                ('Monto_Aprobado', models.FloatField()),
                ('Monto_Fondeado', models.FloatField()),
                ('Plazo_Meses', models.IntegerField()),
                ('Tasa_Anual_fraccion', models.FloatField()),
                ('Fecha_Aprobado', models.DateField()),
                ('Fecha_Liberado', models.DateField()),
                ('Comision_Apertura', models.FloatField()),
                ('Capital_Pagado', models.FloatField()),
                ('Interes_Pagados', models.FloatField()),
                ('Interes_Moratorios_Pagados', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCapital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_usuario', models.IntegerField()),
                ('Sexo', models.CharField(choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10)),
                ('AnioNacimiento', models.DateField()),
                ('Estado', models.CharField(choices=[('B.C.', 'B.C.'), ('B.C.S.', 'B.C.S.'), ('Camp.', 'Camp.'), ('Coah.', 'Coah.'), ('Col.', 'Col.'), ('Chis.', 'Chis.'), ('Chih.', 'Chih.'), ('D.F.', 'D.F.'), ('Dgo.', 'Dgo.'), ('Gto.', 'Gto.')], max_length=10)),
                ('Edad', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserDeuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_usuario', models.IntegerField()),
                ('Sexo', models.CharField(choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10)),
                ('AnioNacimiento', models.DateField()),
                ('Estado', models.CharField(choices=[('B.C.', 'B.C.'), ('B.C.S.', 'B.C.S.'), ('Camp.', 'Camp.'), ('Coah.', 'Coah.'), ('Col.', 'Col.'), ('Chis.', 'Chis.'), ('Chih.', 'Chih.'), ('D.F.', 'D.F.'), ('Dgo.', 'Dgo.'), ('Gto.', 'Gto.')], max_length=10)),
                ('Edad', models.IntegerField()),
                ('Estado_Civil', models.CharField(max_length=10)),
                ('Codigo_Postal', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
