# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 18:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_core', '0007_auto_20170625_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectcapital',
            old_name='Fondeado',
            new_name='Monto_Fondeado',
        ),
        migrations.RenameField(
            model_name='projectdeuda',
            old_name='Fecha_Aprobado',
            new_name='Fecha_Inicio',
        ),
        migrations.RemoveField(
            model_name='projectcapital',
            name='Plazo_Meses',
        ),
        migrations.RemoveField(
            model_name='projectdeuda',
            name='Fecha_Liberado',
        ),
        migrations.RemoveField(
            model_name='projectdeuda',
            name='Plazo_Meses',
        ),
        migrations.AddField(
            model_name='fundingcapital',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fundingdeuda',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fundingdonation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fundingrecompensas',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectcapital',
            name='Plazo_Dias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectcapital',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdeuda',
            name='Fecha_Termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdeuda',
            name='Plazo_Dias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdeuda',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdonation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectrecompesas',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercapital',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdeuda',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdonation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userrecompensas',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fundingdeuda',
            name='Tipo_Movimiento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fundingrecompensas',
            name='Fondeadores',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Categoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Cuota_Comision',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Fecha_Termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectcapital',
            name='Tasa_Interes',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Capital_Pagado',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Categoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Comision_Apertura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Interes_Moratorios_Pagados',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Interes_Pagados',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Monto_Fondeado',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectdeuda',
            name='Tasa_Anual_fraccion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Categoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Fecha_Termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Plazo_Dias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Categoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Fecha_Termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Plazo_Dias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectrecompesas',
            name='Subcategoria',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usercapital',
            name='AnioNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usercapital',
            name='Edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usercapital',
            name='Estado',
            field=models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja_California', 'Baja_California'), ('Baja_California_Sur', 'Baja_California_Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Ciudad_de_Mexico', 'Ciudad_de_Mexico'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Estado_de_Mexico', 'Estado_de_Mexico'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Michoacan', 'Michoacan'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo_Leon', 'Nuevo_Leon'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Queretaro', 'Queretaro'), ('Quintana_Roo', 'Quintana_Roo'), ('San_Luis_Potosi', 'San_Luis_Potosi'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatan', 'Yucatan'), ('Zacatecas', 'Zacatecas')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usercapital',
            name='Sexo',
            field=models.CharField(blank=True, choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdeuda',
            name='AnioNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdeuda',
            name='Codigo_Postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdeuda',
            name='Edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdeuda',
            name='Estado',
            field=models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja_California', 'Baja_California'), ('Baja_California_Sur', 'Baja_California_Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Ciudad_de_Mexico', 'Ciudad_de_Mexico'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Estado_de_Mexico', 'Estado_de_Mexico'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Michoacan', 'Michoacan'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo_Leon', 'Nuevo_Leon'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Queretaro', 'Queretaro'), ('Quintana_Roo', 'Quintana_Roo'), ('San_Luis_Potosi', 'San_Luis_Potosi'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatan', 'Yucatan'), ('Zacatecas', 'Zacatecas')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdeuda',
            name='Estado_Civil',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdeuda',
            name='Sexo',
            field=models.CharField(blank=True, choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdonation',
            name='AnioNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdonation',
            name='Edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdonation',
            name='Estado',
            field=models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja_California', 'Baja_California'), ('Baja_California_Sur', 'Baja_California_Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Ciudad_de_Mexico', 'Ciudad_de_Mexico'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Estado_de_Mexico', 'Estado_de_Mexico'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Michoacan', 'Michoacan'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo_Leon', 'Nuevo_Leon'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Queretaro', 'Queretaro'), ('Quintana_Roo', 'Quintana_Roo'), ('San_Luis_Potosi', 'San_Luis_Potosi'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatan', 'Yucatan'), ('Zacatecas', 'Zacatecas')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdonation',
            name='Sexo',
            field=models.CharField(blank=True, choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userrecompensas',
            name='AnioNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userrecompensas',
            name='Codigo_Postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userrecompensas',
            name='Edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userrecompensas',
            name='Estado',
            field=models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja_California', 'Baja_California'), ('Baja_California_Sur', 'Baja_California_Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Ciudad_de_Mexico', 'Ciudad_de_Mexico'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Estado_de_Mexico', 'Estado_de_Mexico'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Michoacan', 'Michoacan'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo_Leon', 'Nuevo_Leon'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Queretaro', 'Queretaro'), ('Quintana_Roo', 'Quintana_Roo'), ('San_Luis_Potosi', 'San_Luis_Potosi'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatan', 'Yucatan'), ('Zacatecas', 'Zacatecas')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userrecompensas',
            name='Sexo',
            field=models.CharField(blank=True, choices=[('mujer', 'mujer'), ('hombre', 'hombre')], max_length=10, null=True),
        ),
    ]