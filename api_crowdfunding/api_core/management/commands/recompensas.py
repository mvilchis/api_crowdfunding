import pandas as pd
from pandas.core.groupby import GroupBy

from api_core.indexes import (FUNDINGS_CATEGORIES, PROJECTS_CATEGORIES,
                              format_funding_data, format_projects_data,
                              format_users_data, get_acumulado,
                              get_fundind_data, get_indexes, get_projects_data,
                              get_range, get_users_data, merge_data, nunique)
from api_core.mi_cochinito import (get_micochinito_donations,
                                   get_micochinito_donors,
                                   get_micochinito_projects)
from api_core.models import (FundingRecompensas, ProjectRecompesas,
                             UserRecompensas)
from django.core.management.base import BaseCommand

ID = 'i2'


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):
        projects_data_aux = get_micochinito_projects()
        donors = projects_data_aux[[u'Fondeadores', u'IdProyecto']]
        projects_data = format_projects_data(
            pd.concat(
                [get_projects_data(ProjectRecompesas), projects_data_aux]))
        users_data = format_users_data(
            pd.concat(
                [get_users_data(UserRecompensas),
                 get_micochinito_donors()]))
        fundings_data_aux = pd.merge(
            get_micochinito_donations(),
            donors,
            how='left',
            on=[u'IdProyecto'])
        fundings_data = format_funding_data(
            pd.concat(
                [get_fundind_data(FundingRecompensas), fundings_data_aux]))
        projects_users_data, fundings_users_data = merge_data(
            projects_data, users_data, fundings_data)

        succesful_projects_data = projects_users_data.loc[projects_users_data[
            u'ExitoFondeo'] == True]

        range_begin = get_range(projects_users_data, min)
        range_end = get_range(projects_users_data, max)

        indexes = [{
            'dataframe': projects_users_data,
            'operation': GroupBy.size,
            'elements': PROJECTS_CATEGORIES[:-1]
        }, {
            'dataframe': succesful_projects_data,
            'operation': GroupBy.size,
            'elements': PROJECTS_CATEGORIES[:-2]
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.sum,
            'elements': PROJECTS_CATEGORIES[:-2],
            'column': u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': PROJECTS_CATEGORIES[:-1],
            'column': u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': PROJECTS_CATEGORIES[:-2],
            'column': u'ExitoFondeo'
        }, {
            'dataframe': fundings_users_data,
            'operation': GroupBy.sum,
            'elements': FUNDINGS_CATEGORIES,
            'column': u'Fondeadores'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': PROJECTS_CATEGORIES[:-1],
            'column': u'Duracion'
        }]
        get_indexes(
            indexes,
            _id=ID,
            estatal=False,
            range_begin=range_begin,
            range_end=range_end)
