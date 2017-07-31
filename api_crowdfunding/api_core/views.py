# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from serializer import ProjectDonationSerializer, UserDonationSerializer, FundingDonationSerializer
from serializer import ProjectRecompesasSerializer, UserRecompensasSerializer, FundingRecompensasSerializer
from serializer import ProjectCapitalSerializer, UserCapitalSerializer, FundingCapitalSerializer
from serializer import ProjectDeudaSerializer, UserDeudaSerializer, FundingDeudaSerializer

from api_core.models import (ProjectDonation, UserDonation, FundingDonation)
from models import ProjectRecompesas, UserRecompensas, FundingRecompensas
from models import ProjectCapital, UserCapital, FundingCapital
from models import ProjectDeuda, UserDeuda, FundingDeuda

from django.contrib.auth.models import Group
from rest_framework import permissions

# Create your views here.


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    return Group.objects.get(name=group_name).user_set.filter(
        id=user.id).exists()


class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, 'required_groups', {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups.
        return all([
            is_in_group(request.user, group_name)
            for group_name in required_groups
        ])


class ProjectDonationViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Donacion'],
        'POST': ['Donacion'],
    }
    queryset = ProjectDonation.objects.all()
    serializer_class = ProjectDonationSerializer


class UserDonationViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Donacion'],
        'POST': ['Donacion'],
    }
    queryset = UserDonation.objects.all()
    serializer_class = UserDonationSerializer


class FundingDonationViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Donacion'],
        'POST': ['Donacion'],
    }
    queryset = FundingDonation.objects.all()
    serializer_class = FundingDonationSerializer


class ProjectRecompesasViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Recompensas'],
        'POST': ['Recompensas'],
    }
    queryset = ProjectRecompesas.objects.all()
    serializer_class = ProjectRecompesasSerializer


class UserRecompensasViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Recompensas'],
        'POST': ['Recompensas'],
    }
    queryset = UserRecompensas.objects.all()
    serializer_class = UserRecompensasSerializer


class FundingRecompensasViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Recompensas'],
        'POST': ['Recompensas'],
    }
    queryset = FundingRecompensas.objects.all()
    serializer_class = FundingRecompensasSerializer


class ProjectCapitalViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Capital'],
        'POST': ['Capital'],
    }
    queryset = ProjectCapital.objects.all()
    serializer_class = ProjectCapitalSerializer


class UserCapitalViewSet(ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Capital'],
        'POST': ['Capital'],
    }
    queryset = UserCapital.objects.all()
    serializer_class = UserCapitalSerializer


class FundingCapitalViewSet(ModelViewSet):
    required_groups = {
        'GET': ['Capital'],
        'POST': ['Capital'],
    }
    queryset = FundingCapital.objects.all()
    serializer_class = FundingCapitalSerializer


class ProjectDeudaViewSet(ModelViewSet):
    required_groups = {
        'GET': ['Deuda'],
        'POST': ['Deuda'],
    }
    queryset = ProjectDeuda.objects.all()
    serializer_class = ProjectDeudaSerializer


class UserDeudaViewSet(ModelViewSet):
    required_groups = {
        'GET': ['Deuda'],
        'POST': ['Deuda'],
    }
    queryset = UserDeuda.objects.all()
    serializer_class = UserDeudaSerializer


class FundingDeudaViewSet(ModelViewSet):
    required_groups = {
        'GET': ['Deuda'],
        'POST': ['Deuda'],
    }
    queryset = FundingDeuda.objects.all()
    serializer_class = FundingDeudaSerializer
