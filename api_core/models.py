# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
MAN = 'hombre'
WOMAN = 'mujer'

SEX_CHOICES = ((WOMAN, 'mujer'), (MAN, 'hombre'), )

Aguascalientes = 'Aguascalientes'
Baja_California = 'Baja_California'
Baja_California_Sur = 'Baja_California_Sur'
Campeche = 'Campeche'
Chiapas = 'Chiapas'
Chihuahua = 'Chihuahua'
Ciudad_de_Mexico = 'Ciudad_de_Mexico'
Coahuila = 'Coahuila'
Colima = 'Colima'
Durango = 'Durango'
Estado_de_Mexico = 'Estado_de_Mexico'
Guanajuato = 'Guanajuato'
Guerrero = 'Guerrero'
Hidalgo = 'Hidalgo'
Jalisco = 'Jalisco'
Michoacan = 'Michoacan'
Morelos = 'Morelos'
Nayarit = 'Nayarit'
Nuevo_Leon = 'Nuevo_Leon'
Oaxaca = 'Oaxaca'
Puebla = 'Puebla'
Queretaro = 'Queretaro'
Quintana_Roo = 'Quintana_Roo'
San_Luis_Potosi = 'San_Luis_Potosi'
Sinaloa = 'Sinaloa'
Sonora = 'Sonora'
Tabasco = 'Tabasco'
Tamaulipas = 'Tamaulipas'
Tlaxcala = 'Tlaxcala'
Veracruz = 'Veracruz'
Yucatan = 'Yucatan'
Zacatecas = 'Zacatecas'

COUNTRY_CHOICES = (
    (Aguascalientes, Aguascalientes), (Baja_California, Baja_California),
    (Baja_California_Sur, Baja_California_Sur), (Campeche, Campeche),
    (Chiapas, Chiapas), (Chihuahua, Chihuahua),
    (Ciudad_de_Mexico, Ciudad_de_Mexico), (Coahuila, Coahuila),
    (Colima, Colima), (Durango, Durango), (Estado_de_Mexico, Estado_de_Mexico),
    (Guanajuato, Guanajuato), (Guerrero, Guerrero), (Hidalgo, Hidalgo),
    (Jalisco, Jalisco), (Michoacan, Michoacan), (Morelos, Morelos),
    (Nayarit, Nayarit), (Nuevo_Leon, Nuevo_Leon), (Oaxaca, Oaxaca),
    (Puebla, Puebla), (Queretaro, Queretaro), (Quintana_Roo, Quintana_Roo),
    (San_Luis_Potosi, San_Luis_Potosi), (Sinaloa, Sinaloa), (Sonora, Sonora),
    (Tabasco, Tabasco), (Tamaulipas, Tamaulipas), (Tlaxcala, Tlaxcala),
    (Veracruz, Veracruz), (Yucatan, Yucatan), (Zacatecas, Zacatecas))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class Project(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey(User, null = True)
    ID_Proyecto = models.IntegerField()
    ID_Usuario = models.IntegerField()
    Categoria = models.CharField(max_length=10, blank=True, null=True)
    Subcategoria = models.CharField(max_length=10,  blank=True, null=True)


class ProjectDonation(Project):
    Plazo_Dias = models.IntegerField( blank=True, null=True)
    Fecha_Inicio = models.DateField()
    Fecha_Termino = models.DateField( blank=True, null=True)
    Monto_Recaudado = models.FloatField()


class ProjectRecompesas(Project):
    Plazo_Dias = models.IntegerField( blank=True, null=True)
    Fecha_Inicio = models.DateField()
    Fecha_Termino = models.DateField( blank=True, null=True)
    Monto_Recaudado = models.FloatField()


class ProjectCapital(Project):
    Monto_Aprobado = models.FloatField()
    Monto_Recaudado = models.FloatField()
    Monto_Fondeado = models.BooleanField( blank=True)
    Fecha_Inicio = models.DateField()
    Fecha_Termino = models.DateField( blank=True, null=True)
    Plazo_Dias = models.IntegerField( blank=True, null=True)
    Tasa_Interes = models.FloatField( blank=True, null=True)
    Cuota_Comision = models.FloatField( blank=True, null=True)


class ProjectDeuda(Project):
    Monto_Aprobado = models.FloatField()
    Monto_Fondeado = models.FloatField( blank=True, null=True)
    Plazo_Dias = models.IntegerField( blank=True, null=True)
    Tasa_Anual_fraccion = models.FloatField( blank=True, null=True)
    Fecha_Termino = models.DateField( blank=True, null=True)
    Fecha_Inicio = models.DateField()
    Comision_Apertura = models.FloatField( blank=True, null=True)
    Capital_Pagado = models.FloatField( blank=True, null=True)
    Interes_Pagados = models.FloatField( blank=True, null=True)
    Interes_Moratorios_Pagados = models.FloatField( blank=True, null=True)


class UserProject(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, null =True)
    ID_usuario = models.IntegerField()
    Sexo = models.CharField(max_length=10, choices=SEX_CHOICES, blank=True, null=True)
    AnioNacimiento = models.DateField( blank=True, null=True)
    Estado = models.CharField(max_length=10, choices=COUNTRY_CHOICES, blank=True, null=True)
    Edad = models.IntegerField( blank=True, null=True)


class UserDonation(UserProject):
    pass


class UserRecompensas(UserProject):
    Codigo_Postal = models.IntegerField( blank=True, null=True)


class UserCapital(UserProject):
    pass


class UserDeuda(UserProject):
    Estado_Civil = models.CharField(max_length=10, blank=True, null=True)
    Codigo_Postal = models.IntegerField( blank=True, null=True)


class Funding(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey(User,null = True)
    ID_Proyecto = models.IntegerField()
    ID_Usuario = models.IntegerField()
    Monto_Recaudado = models.FloatField()
    Fecha = models.DateField()


class FundingDonation(Funding):
    pass


class FundingRecompensas(Funding):
    Fondeadores = models.IntegerField( blank=True, null=True)
    Exito_Fondeo = models.BooleanField(blank=True)


class FundingCapital(Funding):
    pass


class FundingDeuda(Funding):
    Tipo_Movimiento = models.CharField(max_length=10, blank=True, null=True)
