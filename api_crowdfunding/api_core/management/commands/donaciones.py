import pandas as pd
from pandas.core.groupby import GroupBy

from api_core.indexes import (
    FUNDINGS_CATEGORIES, PROJECTS_CATEGORIES, format_funding_data,
    format_projects_data, format_users_data, get_acumulado, get_fundind_data,
    get_indexes, get_projects_data, get_users_data, merge_data, nunique)
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
            'elements': PROJECTS_CATEGORIES[:-1]
        }, {
            'dataframe': succesful_projects_data,
            'operation': GroupBy.size,
            'elements': PROJECTS_CATEGORIES[:-2]
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.sum,
            'elements': PROJECTS_CATEGORIES[:-1],
            'column': u'MontoRecaudado'
        }, {
            'dataframe': projects_users_data,
            'operation': GroupBy.mean,
            'elements': PROJECTS_CATEGORIES[:-2],
            'column': u'ExitoFondeo'
        }, {
            'dataframe': fundings_users_data,
            'operation': nunique,
            'elements': FUNDINGS_CATEGORIES,
            'column': u'IdUsuario'
        }, {
            'dataframe': fundings_users_data,
            'operation': GroupBy.mean,
            'elements': FUNDINGS_CATEGORIES,
            'column': u'MontoRecaudado'
        }]
        get_indexes(indexes, _id=ID, estatal=False)
