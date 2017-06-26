# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

HORROR = 'horror'
COMEDY = 'comedy'
ACTION = 'action'
DRAMA = 'drama'

CATEGORIES_CHOICES = ((HORROR, 'Horror'), (COMEDY, 'Comedy'),
                      (ACTION, 'Action'), (DRAMA, 'Drama'), )

MAN = 'hombre'
WOMAN = 'mujer'

SEX_CHOICES = ((WOMAN, 'mujer'), (MAN, 'hombre'), )

Aguascalientes = 'Aguascalientes'
Baja_California = 'Baja California'
Baja_California_Sur = 'Baja_California_Sur'
Campeche = 'Campeche'
Chiapas = 'Chiapas'
Chihuahua = 'Chihuahua'
Ciudad_de_Mexico = 'Ciudad de México'
Coahuila = 'Coahuila'
Colima = 'Colima'
Durango = 'Durango'
Estado_de_Mexico = 'Estado de México'
Guanajuato = 'Guanajuato'
Guerrero = 'Guerrero'
Hidalgo = 'Hidalgo'
Jalisco = 'Jalisco'
Michoacan = 'Michoacán'
Morelos = 'Morelos'
Nayarit = 'Nayarit'
Nuevo_Leon = 'Nuevo León'
Oaxaca = 'Oaxaca'
Puebla = 'Puebla'
Queretaro = 'Querétaro'
Quintana_Roo = 'Quintana Roo'
San_Luis_Potosi = 'San Luis Potosí'
Sinaloa = 'Sinaloa'
Sonora = 'Sonora'
Tabasco = 'Tabasco'
Tamaulipas = 'Tamaulipas'
Tlaxcala = 'Tlaxcala'
Veracruz = 'Veracruz'
Yucatan = 'Yucatán'
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

    ID_Proyecto = models.IntegerField()
    ID_Usuario = models.IntegerField()
    Categoria = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    Subcategoria = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)


class ProjectDonation(Project):
    Plazo_Dias = models.IntegerField()
    Fecha_Inicio = models.DateField()
    Fecha_Termino = models.DateField()
    Monto_Recaudado = models.FloatField()


class ProjectRecompesas(Project):
    Plazo_Dias = models.IntegerField()
    Fecha_Inicio = models.DateField()
    Fecha_Termino = models.DateField()
    Monto_Recaudado = models.FloatField()


class ProjectCapital(Project):
    Monto_Aprobado = models.FloatField()
    Plazo_Meses = models.IntegerField()
    Tasa_Interes = models.FloatField()
    Fecha_Inicio = models.DateField()
    Fecha_Termino = models.DateField()
    Monto_Recaudado = models.FloatField()
    Cuota_Comision = models.FloatField()
    Fondeado = models.BooleanField()


class ProjectDeuda(Project):
    Monto_Aprobado = models.FloatField()
    Monto_Fondeado = models.FloatField()
    Plazo_Meses = models.IntegerField()
    Tasa_Anual_fraccion = models.FloatField()
    Fecha_Aprobado = models.DateField()
    Fecha_Liberado = models.DateField()
    Comision_Apertura = models.FloatField()
    Capital_Pagado = models.FloatField()
    Interes_Pagados = models.FloatField()
    Interes_Moratorios_Pagados = models.FloatField()


class UserProject(models.Model):
    class Meta:
        abstract = True

    ID_usuario = models.IntegerField()
    Sexo = models.CharField(max_length=10, choices=SEX_CHOICES)
    AnioNacimiento = models.DateField()
    Estado = models.CharField(max_length=10, choices=COUNTRY_CHOICES)

    Edad = models.IntegerField()


class UserDonation(UserProject):
    pass


class UserRecompensas(UserProject):
    Codigo_Postal = models.IntegerField()


class UserCapital(UserProject):
    pass


class UserDeuda(UserProject):
    Estado_Civil = models.CharField(max_length=10)
    Codigo_Postal = models.IntegerField()


class Funding(models.Model):
    class Meta:
        abstract = True

    ID_Proyecto = models.IntegerField()
    ID_Usuario = models.IntegerField()
    Monto_Recaudado = models.FloatField()
    Fecha = models.DateField()


class FundingDonation(Funding):
    pass


class FundingRecompensas(Funding):
    Fondeadores = models.IntegerField()
    Exito_Fondeo = models.BooleanField()


class FundingCapital(Funding):
    pass


class FundingDeuda(Funding):
    Tipo_Movimiento = models.CharField(max_length=10)
