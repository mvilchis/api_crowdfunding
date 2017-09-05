import numpy as np
import pandas as pd

from api_core.models import FundingDeuda, ProjectDeuda, User, UserDeuda
from django.core.management.base import BaseCommand


def get_CP():
    #url = "http://www.correosdemexico.gob.mx/datosabiertos/cp/cpdescarga.txt"
    url = 'cpdescarga.txt'
    CP = pd.read_csv(url, sep='|', skiprows=1)

    CP = CP[[u'd_codigo', u'c_estado']].drop_duplicates().rename(
        columns={"d_codigo": "CodigoPostal",
                 "c_estado": "cve"})
    return CP


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):

        projects = pd.DataFrame(list(ProjectDeuda.objects.all().values()))
        users = pd.DataFrame(list(UserDeuda.objects.all().values()))
        funding = pd.DataFrame(list(FundingDeuda.objects.all().values()))

        projects['IdUsuario'] = projects['user_id'].astype(
            str) + '-' + projects['IdUsuario'].astype(str)
        projects['IdProyecto'] = projects['user_id'].astype(
            str) + '-' + projects['IdProyecto'].astype(str)
        users['IdUsuario'] = users['user_id'].astype(
            str) + '-' + users['IdUsuario'].astype(str)
        funding['IdUsuario'] = funding['user_id'].astype(
            str) + '-' + funding['IdUsuario'].astype(str)
        funding['IdProyecto'] = funding['user_id'].astype(
            str) + '-' + funding['IdProyecto'].astype(str)

        CP = get_CP()

        users = pd.merge(users, CP, how='left', on=[u'CodigoPostal'])

        projects[u'plazo_meses'] = projects[u'PlazoDias'] // 30

        Prestadero = pd.merge(projects, users, how='left', on=[u'IdUsuario'])

        PrestaderoFondeadore = pd.merge(
            funding, projects, how='left', on=[u'IdUsuario'])

        Prestadero[u'fecha_aprobado'] = pd.to_datetime(
            Prestadero[u'FechaTermino'])
        Prestadero[u'anio'] = Prestadero[u'fecha_aprobado'].map(
            lambda x: x.year).fillna(0).astype(np.int64)
        Prestadero[u'mes'] = Prestadero[u'fecha_aprobado'].map(
            lambda x: x.month).fillna(0).astype(np.int64)

        T1 = Prestadero.groupby([u'anio', u'mes']).size().reset_index(
            name="ProyectosTotales")
        T1['cve'] = 0

        T1_a = Prestadero.groupby([u'anio', u'mes',
                                   u'Categoria']).size().reset_index(
                                       name="ProyectosTotales")
        T1_a['cve'] = 0

        Prestadero[u'genero'] = Prestadero[u'Genero'].fillna("")
        # Prestadero.loc[Prestadero[u'Genero'] == 'M', u'genero'] = "Masculino"
