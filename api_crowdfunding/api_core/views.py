# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

#############   REST Libraries      ##########
#from rest_framework.viewsets import ListBulkCreateUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView


#############      My libraries     ##########
from serializer import (ProjectDonationSerializer,
                        ProjectDeudaSerializer,
                        ProjectRecompesasSerializer,
                        ProjectCapitalSerializer,
                        UserDonationSerializer,
                        UserRecompensasSerializer,
                        UserCapitalSerializer,
                        UserDeudaSerializer,
                        FundingDonationSerializer,
                        FundingRecompensasSerializer,
                        FundingCapitalSerializer,
                        FundingDeudaSerializer,)
from models     import (ProjectDonation,
                        ProjectRecompesas,
                        ProjectCapital,
                        ProjectDeuda,
                        UserDonation,
                        UserRecompensas,
                        UserCapital,
                        UserDeuda,
                        FundingDonation,
                        FundingRecompensas,
                        FundingCapital,
                        FundingDeuda)

from django.contrib.auth.models import Group

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


class ProjectDonationViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Donacion'],
        'POST': ['Donacion'],
    }
    queryset = ProjectDonation.objects.all()
    serializer_class = ProjectDonationSerializer


class UserDonationViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Donacion'],
        'POST': ['Donacion'],
    }
    queryset = UserDonation.objects.all()
    serializer_class = UserDonationSerializer


class FundingDonationViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Donacion'],
        'POST': ['Donacion'],
    }
    queryset = FundingDonation.objects.all()
    serializer_class = FundingDonationSerializer


class ProjectRecompesasViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Recompensas'],
        'POST': ['Recompensas'],
    }
    queryset = ProjectRecompesas.objects.all()
    serializer_class = ProjectRecompesasSerializer


class UserRecompensasViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Recompensas'],
        'POST': ['Recompensas'],
    }
    queryset = UserRecompensas.objects.all()
    serializer_class = UserRecompensasSerializer


class FundingRecompensasViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Recompensas'],
        'POST': ['Recompensas'],
    }
    queryset = FundingRecompensas.objects.all()
    serializer_class = FundingRecompensasSerializer


class ProjectCapitalViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Capital'],
        'POST': ['Capital'],
    }
    queryset = ProjectCapital.objects.all()
    serializer_class = ProjectCapitalSerializer


class UserCapitalViewSet(ListBulkCreateUpdateDestroyAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Capital'],
        'POST': ['Capital'],
    }
    queryset = UserCapital.objects.all()
    serializer_class = UserCapitalSerializer


class FundingCapitalViewSet(ListBulkCreateUpdateDestroyAPIView):
    required_groups = {
        'GET': ['Capital'],
        'POST': ['Capital'],
    }
    queryset = FundingCapital.objects.all()
    serializer_class = FundingCapitalSerializer


class ProjectDeudaViewSet(ListBulkCreateUpdateDestroyAPIView):
    required_groups = {
        'GET': ['Deuda'],
        'POST': ['Deuda'],
    }
    queryset = ProjectDeuda.objects.all()
    serializer_class = ProjectDeudaSerializer


class UserDeudaViewSet(ListBulkCreateUpdateDestroyAPIView):
    required_groups = {
        'GET': ['Deuda'],
        'POST': ['Deuda'],
    }
    queryset = UserDeuda.objects.all()
    serializer_class = UserDeudaSerializer


class FundingDeudaViewSet(ListBulkCreateUpdateDestroyAPIView):
    required_groups = {
        'GET': ['Deuda'],
        'POST': ['Deuda'],
    }
    queryset = FundingDeuda.objects.all()
    serializer_class = FundingDeudaSerializer
