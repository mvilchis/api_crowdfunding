# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from serializer import ProjectDonationSerializer, UserDonationSerializer, FundingDonationSerializer
from serializer import ProjectRecompesasSerializer, UserRecompensasSerializer, FundingRecompensasSerializer
from serializer import ProjectCapitalSerializer, UserCapitalSerializer, FundingCapitalSerializer
from serializer import ProjectDeudaSerializer, UserDeudaSerializer, FundingDeudaSerializer

from models import ProjectDonation, UserDonation, FundingDonation
from models import ProjectRecompesas, UserRecompensas, FundingRecompensas
from models import ProjectCapital, UserCapital, FundingCapital
from models import ProjectDeuda, UserDeuda, FundingDeuda

# Create your views here.


class ProjectDonationViewSet(ModelViewSet):
    queryset = ProjectDonation.objects.all()
    serializer_class = ProjectDonationSerializer


class UserDonationViewSet(ModelViewSet):
    queryset = UserDonation.objects.all()
    serializer_class = UserDonationSerializer


class FundingDonationViewSet(ModelViewSet):
    queryset = FundingDonation.objects.all()
    serializer_class = FundingDonationSerializer


class ProjectRecompesasViewSet(ModelViewSet):
    queryset = ProjectRecompesas.objects.all()
    serializer_class = ProjectRecompesasSerializer


class UserRecompensasViewSet(ModelViewSet):
    queryset = UserRecompensas.objects.all()
    serializer_class = UserRecompensasSerializer


class FundingRecompensasViewSet(ModelViewSet):
    queryset = FundingRecompensas.objects.all()
    serializer_class = FundingRecompensasSerializer


class ProjectCapitalViewSet(ModelViewSet):
    queryset = ProjectCapital.objects.all()
    serializer_class = ProjectCapitalSerializer


class UserCapitalViewSet(ModelViewSet):
    queryset = UserCapital.objects.all()
    serializer_class = UserCapitalSerializer


class FundingCapitalViewSet(ModelViewSet):
    queryset = FundingCapital.objects.all()
    serializer_class = FundingCapitalSerializer


class ProjectDeudaViewSet(ModelViewSet):
    queryset = ProjectDeuda.objects.all()
    serializer_class = ProjectDeudaSerializer


class UserDeudaViewSet(ModelViewSet):
    queryset = UserDeuda.objects.all()
    serializer_class = UserDeudaSerializer


class FundingDeudaViewSet(ModelViewSet):
    queryset = FundingDeuda.objects.all()
    serializer_class = FundingDeudaSerializer
