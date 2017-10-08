#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import sys

import numpy as np
import pandas as pd
from pandas.core.groupby import GroupBy

from api_core.indexes2 import (format_funding_data, format_projects_data,
                               format_users_data, get_fundind_data,
                               get_indexes, get_projects_data, get_users_data,
                               merge_data, nunique)
from api_core.mi_cochinito import (get_micochinito_donations,
                                   get_micochinito_donors,
                                   get_micochinito_projects)
from api_core.models import FundingDonation, ProjectDonation, UserDonation
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):
        projects_data = format_projects_data(
            pd.concat([
                get_projects_data(ProjectDonation),
                get_micochinito_projects()
            ]))
        users_data = format_users_data(
            pd.concat([get_users_data(UserDonation),
                       get_micochinito_donors()]))
        fundings_data = format_funding_data(
            pd.concat([
                get_fundind_data(FundingDonation),
                get_micochinito_donations()
            ]))

        #Adding user info
        projects_users_data, fundings_users_data = merge_data(
            projects_data, users_data, fundings_data)

        succesful_projects_data = projects_users_data.loc[projects_users_data[
            u'ExitoFondeo'] == True]

        indexes = [{
            'dataframe': projects_users_data,
            '_id': 'i31',
            'operation': GroupBy.size,
            'elements': [u'Total', u'Categoria', 'Genero']
        }, {
            'dataframe': succesful_projects_data,
            '_id': 'i32',
            'operation': GroupBy.size,
            'elements': [u'Total', u'Categoria', 'Genero']
        }, {
            'dataframe':
            projects_users_data,
            '_id':
            'i33',
            'operation':
            GroupBy.sum,
            'elements': [u'Total', u'Categoria', 'Genero', u'ExitoFondeo'],
            'column':
            u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            '_id': 'i34',
            'operation': GroupBy.mean,
            'elements': [u'Total', u'Categoria', 'Genero'],
            'column': u'ExitoFondeo'
        }, {
            'dataframe': fundings_users_data,
            '_id': 'i35',
            'operation': nunique,
            'elements': [u'Total', 'Genero'],
            'column': u'IdUsuario'
        }, {
            'dataframe': fundings_users_data,
            '_id': 'i36',
            'operation': GroupBy.mean,
            'elements': [u'Total', 'Genero'],
            'column': u'MontoRecaudado'
        }]

        data, ID2, DesGeo, RangeT = get_indexes(indexes, estatal=False)

        data.to_csv(
            'DonacionesData2.csv',
            index=False,
            columns=["id", "m", "t", "valor", "id2", "cve", "DesGeo"])
        ID2.to_csv('DonacionesCodigosGrupos2.csv', index=False)
        DesGeo.to_csv('DonacionesDesGeo2.csv', index=False)
        RangeT.to_csv('DonacionesRangosTemporales2.csv', index=False)
