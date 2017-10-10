import pandas as pd
from pandas.core.groupby import GroupBy

from api_core.indexes import (format_funding_data, format_projects_data,
                              format_users_data, get_acumulado,
                              get_fundind_data, get_indexes, get_projects_data,
                              get_users_data, merge_data, nunique, save_data)
from api_core.models import FundingDonation, ProjectDonation, UserDonation
from django.core.management.base import BaseCommand

ID = 'i3'


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):
        projects_data = format_projects_data(
            get_projects_data(ProjectDonation))
        users_data = format_users_data(get_users_data(UserDonation))
        fundings_data = format_funding_data(get_fundind_data(FundingDonation))

        projects_users_data, fundings_users_data = merge_data(
            projects_data, users_data, fundings_data)

        #Adding user info
        projects_users_data, fundings_users_data = merge_data(
            projects_data, users_data, fundings_data)

        succesful_projects_data = projects_users_data.loc[projects_users_data[
            u'ExitoFondeo'] == True]

        indexes = [{
            'dataframe': projects_users_data,
            'operation': GroupBy.size,
            'elements': [u'Total', u'Categoria', 'Genero']
        }, {
            'dataframe': succesful_projects_data,
            'operation': GroupBy.size,
            'elements': [u'Total', u'Categoria', 'Genero']
        }, {
            'dataframe':
            projects_users_data,
            'operation':
            GroupBy.sum,
            'elements': [u'Total', u'Categoria', 'Genero', u'ExitoFondeo'],
            'column':
            u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': [u'Total', u'Categoria', 'Genero'],
            'column': u'ExitoFondeo'
        }, {
            'dataframe': fundings_users_data,
            'operation': nunique,
            'elements': [u'Total', 'Genero'],
            'column': u'IdUsuario'
        }, {
            'dataframe': fundings_users_data,
            'operation': GroupBy.mean,
            'elements': [u'Total', 'Genero'],
            'column': u'MontoRecaudado'
        }]

        data, ID2, DesGeo, RangeT = get_indexes(indexes, _id=ID, estatal=False)
        save_data(ID, data, ID2, DesGeo, RangeT)
        get_acumulado(data, ID)
