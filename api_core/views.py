# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from serializer import ProyectDonationSerializer,  UserDonationSerializer, FundingDonationSerializer
from models import ProyectDonation, UserDonation, FundingDonation
# Create your views here.

class ProyectDonationViewSet(ModelViewSet):
    queryset = ProyectDonation.objects.all()
    serializer_class = ProyectDonationSerializer


class UserDonationViewSet(ModelViewSet):
    queryset = UserDonation.objects.all()
    serializer_class = UserDonationSerializer

class FundingDonationViewSet(ModelViewSet):
    queryset = FundingDonation.objects.all()
    serializer_class = FundingDonationSerializer
