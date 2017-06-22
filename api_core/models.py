# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProyectDonation(models.Model):
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'
    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )
    ID_Proyecto     =  models.IntegerField()
    ID_usuario      =  models.IntegerField()
    Categoria       =  models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    Subcategoria    =  models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    Monto_pedido    =  models.FloatField()
    Monto_aprobado  =  models.FloatField()
    Monto_recaudado =  models.FloatField()
    Plazo_dias      =  models.IntegerField()
    Tasa_de_interes =  models.CharField(max_length=100)
    Fecha_inicio    =  models.DateField()
    Fecha_termino   =  models.DateField()
    Cuota           =  models.FloatField()
    Comision        =  models.FloatField()


class UserDonation(models.Model):
    MAN = 'hombre'
    WOMAN = 'mujer'
    Baja_California       ="B.C."
    Baja_California_Sur   ="B.C.S."
    Campeche              ="Camp."
    Coahuila              ="Coah."
    Colima                ="Col."
    Chiapas               ="Chis."
    Chihuahua             ="Chih."
    Distrito_Federal      ="D.F."
    Durango               ="Dgo."
    Guanajuato            ="Gto."
    SEX_CHOICES = (
        (WOMAN, 'mujer'),
        (MAN, 'hombre'),
    )
    COUNTRY_CHOICES =(
        (Baja_California     ,"B.C."),
        (Baja_California_Sur ,"B.C.S."),
        (Campeche            ,"Camp."),
        (Coahuila            ,"Coah."),
        (Colima              ,"Col."),
        (Chiapas             ,"Chis."),
        (Chihuahua           ,"Chih."),
        (Distrito_Federal    ,"D.F."),
        (Durango             ,"Dgo."),
        (Guanajuato          ,"Gto."),
    )
    ID_usuario     = models.IntegerField()
    Sexo           = models.CharField(max_length=10, choices=SEX_CHOICES)
    AnioNacimiento = models.DateField()
    Estado         = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    Edad           = models.IntegerField()

class FundingDonation(models.Model):
    ID_Proyecto     =  models.IntegerField()
    ID_usuario      =  models.IntegerField()
    Monto_recaudado =  models.FloatField()
    Fecha           = models.DateField()
