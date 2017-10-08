# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .states import *

MAN = 'hombre'
WOMAN = 'mujer'

SEX_CHOICES = (("M", 'H'), ("F", 'F'), ("Masculino", "M"), ("Femenino", "F"),
               ('Hombre', "H"), ("Mujer", "F"))

ESTADO_CIVIL = (("Soltero", "soltero"), ("Casado", "casado"),
                ("casado", "casado"), ("soltero", "soltero"))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class Project(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, null=True)
    IdProyecto = models.IntegerField()
    IdUsuario = models.IntegerField()
    MontoRecaudado = models.FloatField()
    MontoPedido = models.FloatField()
    FechaInicio = models.DateField()
    Categoria = models.CharField(max_length=15, blank=True, null=True)
    Subcategoria = models.CharField(max_length=15, blank=True, null=True)
    FechaTermino = models.DateField(blank=True, null=True)
    PlazoDias = models.IntegerField(blank=True, null=True)
    TasaInteresAnual = models.FloatField(blank=True, null=True)
    CuotaComision = models.FloatField(blank=True, null=True)

    #class Meta:
    #    unique_together = (("user", "ID_Proyecto", "ID_Usuario",
    #                        "Fecha_Inicio", "Monto_Recaudado"), )


class ProjectDonation(Project):
    pass


class ProjectRecompesas(Project):
    pass


class ProjectCapital(Project):
    pass


class ProjectDeuda(Project):
    pass


class UserProject(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, null=True)
    IdUsuario = models.IntegerField()
    Genero = models.CharField(
        max_length=10, choices=SEX_CHOICES, blank=True, null=True)
    FechaNacimiento = models.DateField(blank=True, null=True)
    Estado = models.CharField(
        max_length=10, choices=COUNTRY_CHOICES, blank=True, null=True)
    Edad = models.IntegerField(blank=True, null=True)
    CodigoPostal = models.IntegerField(blank=True, null=True)
    EstadoCivil = models.CharField(max_length=10, blank=True, null=True)
    #class Meta:
    #    unique_together = (("user", "ID_usuario"), )


class UserDonation(UserProject):
    pass


class UserRecompensas(UserProject):
    pass


class UserCapital(UserProject):
    pass


class UserDeuda(UserProject):
    pass


class Funding(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, null=True)
    IdProyecto = models.IntegerField()
    IdUsuario = models.IntegerField()
    MontoRecaudado = models.FloatField()
    Fecha = models.DateField()
    Fondeadores = models.IntegerField(blank=True, null=True)
    ExitoFondeo = models.NullBooleanField()


class FundingDonation(Funding):
    pass


class FundingRecompensas(Funding):
    pass


class FundingCapital(Funding):
    pass


class FundingDeuda(Funding):
    pass
