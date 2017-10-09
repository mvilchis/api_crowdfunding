from pandas.core.groupby import GroupBy

from api_core.indexes import (format_funding_data, format_projects_data,
                              format_users_data, get_acumulado,
                              get_fundind_data, get_indexes, get_projects_data,
                              get_users_data, merge_data, nunique, save_data)
from api_core.models import (FundingRecompensas, ProjectRecompesas,
                             UserRecompensas)
from django.core.management.base import BaseCommand

ID = 'i2'
NAME = 'Recompensas'


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):

        projects_data = format_projects_data(
            get_projects_data(ProjectRecompesas))
        users_data = format_users_data(get_users_data(UserRecompensas))
        fundings_data = format_funding_data(
            get_fundind_data(FundingRecompensas))

        projects_users_data, fundings_users_data = merge_data(
            projects_data, users_data, fundings_data)

        succesful_projects_data = projects_users_data.loc[projects_users_data[
            u'ExitoFondeo'] == True]

        indexes = [{
            'dataframe': projects_users_data,
            'operation': GroupBy.size,
            'elements': [u'Total', u'Categoria']
        }, {
            'dataframe': succesful_projects_data,
            'operation': GroupBy.size,
            'elements': [u'Total', u'Categoria']
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.sum,
            'elements': [u'Total', u'Categoria', u'ExitoFondeo'],
            'column': u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': [u'Total', u'Categoria', u'ExitoFondeo'],
            'column': u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': [u'Total', u'Categoria'],
            'column': u'ExitoFondeo'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.sum,
            'elements': [u'Total'],
            'column': u'Fondeadores'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': [u'Total', 'Categoria'],
            'column': u'Duracion'
        }]
        data, ID2, DesGeo, RangeT = get_indexes(indexes, _id=ID, estatal=True)
        save_data(NAME, data, ID2, DesGeo, RangeT)
        get_acumulado(data, NAME)
