import string

import numpy as np
import pandas as pd
from pandas.core.groupby import GroupBy

from api_core.indexes2 import (format_funding_data, format_projects_data,
                               format_users_data, get_fundind_data,
                               get_indexes, get_projects_data, get_users_data,
                               merge_data, nunique)
from api_core.models import FundingDeuda, ProjectDeuda, User, UserDeuda
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):

        projects_data = format_projects_data(get_projects_data(ProjectDeuda))
        users_data = format_users_data(get_users_data(UserDeuda))
        fundings_data = format_funding_data(get_fundind_data(FundingDeuda))

        projects_users_data, fundings_users_data = merge_data(
            projects_data, users_data, fundings_data)

        succesful_projects_data = projects_users_data.loc[projects_users_data[
            u'ExitoFondeo'] == True]

        indexes = [{
            'dataframe':
            projects_users_data,
            '_id':
            'i11',
            'operation':
            GroupBy.size,
            'elements': [u'Total', u'Categoria', 'Genero', 'EstadoCivil']
        }, {
            'dataframe':
            succesful_projects_data,
            '_id':
            'i12',
            'operation':
            GroupBy.size,
            'elements': [u'Total', u'Categoria', 'Genero', 'EstadoCivil']
        }, {
            'dataframe':
            projects_users_data,
            '_id':
            'i13',
            'operation':
            GroupBy.sum,
            'elements': [u'Total', u'Categoria', 'Genero', u'EstadoCivil'],
            'column':
            u'MontoRecaudado'
        }, {
            'dataframe':
            projects_users_data,
            '_id':
            'i14',
            'operation':
            GroupBy.mean,
            'elements': [u'Total', u'Categoria', 'Genero', u'EstadoCivil'],
            'column':
            u'MontoRecaudado'
        }, {
            'dataframe': succesful_projects_data,
            '_id': 'i14',
            'operation': GroupBy.mean,
            'elements': [u'Total'],
            'column': u'MontoRecaudado'
        }, {
            'dataframe':
            projects_users_data,
            '_id':
            'i15',
            'operation':
            GroupBy.mean,
            'elements': [u'Total', u'Categoria', 'Genero', 'EstadoCivil'],
            'column':
            u'ExitoFondeo'
        }, {
            'dataframe':
            projects_users_data,
            '_id':
            'i16',
            'operation':
            GroupBy.mean,
            'elements': [
                u'Total', u'Categoria', 'Genero', 'EstadoCivil',
                u'ExitoFondeo', u'Plazo'
            ],
            'column':
            u'TasaInteresAnual'
        }, {
            'dataframe': fundings_users_data,
            '_id': 'i17',
            'operation': nunique,
            'elements': [u'Total'],
            'column': u'IdUsuario'
        }, {
            'dataframe':
            projects_users_data,
            '_id':
            'i18',
            'operation':
            GroupBy.mean,
            'elements':
            [u'Total', 'Categoria', 'Genero', 'EstadoCivil', 'ExitoFondeo'],
            'column':
            u'Duracion'
        }]
        data, ID2, DesGeo, RangeT = get_indexes(indexes, estatal=True)
        data.to_csv(
            'DeudaData2.csv',
            index=False,
            columns=["id", "m", "t", "valor", "id2", "cve", "DesGeo"])
        ID2.to_csv('DeudaCodigosGrupos2.csv', index=False)
        DesGeo.to_csv('DeudaDesGeo2.csv', index=False)
        RangeT.to_csv('DeudaRangosTemporales2.csv', index=False)
