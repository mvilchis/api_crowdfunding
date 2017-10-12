import string
import sys

import numpy as np
import pandas as pd

# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

nunique = lambda x: x.nunique()

DATA_PATH = 'data/'
FORMAT = ["id", "m", "t", "valor", "id2", "cve", "DesGeo"]
PROJECTS_CATEGORIES = [
    u'Total', u'Categoria', 'Genero', u'EstadoCivil', u'ExitoFondeo', u'Plazo'
]
FUNDINGS_CATEGORIES = [u'Total', 'Genero', u'EstadoCivil']


def get_CP():
    #url = "http://www.correosdemexico.gob.mx/datosabiertos/cp/cpdescarga.txt"
    url = 'cpdescarga.txt'
    CP = pd.read_csv(url, sep='|', skiprows=1)

    CP = CP[[u'd_codigo', u'c_estado']].drop_duplicates().rename(
        columns={"d_codigo": "CodigoPostal",
                 'c_estado': 'cve'})
    return CP


def get_index_data_aux(groupby, operation, column=None):
    if column:
        return operation(groupby[column])
    else:
        return operation(groupby)


def get_index_data(dataframe,
                   _id,
                   operation,
                   elements,
                   column=None,
                   estatal=False):
    data = []
    for element in elements:
        columns = [u't', u'm', 'cve'] if estatal else [u't', u'm']
        if element != 'Total':
            columns.append(element)
        data_e = get_index_data_aux(
            dataframe.groupby(columns), operation, column).reset_index(
                name="valor")
        if element == 'Total':
            data_e['id3'] = 'Total'
        else:
            data_e['id3'] = element + '-' + data_e[element].map(str)
            del data_e[element]
        data.append(data_e)

    data = pd.concat(data)
    data['id'] = _id
    return data


def get_ids2(data):
    ids2 = []
    for id_name, dt in data[[u'id', u'id3']].drop_duplicates().groupby('id'):
        mapping_ids2 = dict(
            zip(dt[u'id3'].unique(), string.lowercase +
                string.ascii_uppercase))
        dt['id2'] = dt['id3'].map(lambda x: mapping_ids2[x])
        ids2.append(dt)
    return pd.concat(ids2)


def homologate_field(data, field):
    data[field] = data['user_id'].astype(str) + '-' + data[field].astype(str)
    return data


def get_year_and_month(data, field):
    data[field] = pd.to_datetime(data[field])
    data[u't'] = data[field].map(lambda x: x.year)
    data[u'm'] = data[field].map(lambda x: x.month)
    data[u'm'] = data[u'm'].map(
        lambda x: 1 if x < 4 else 2 if x < 7 else 3 if x < 9 else 4)
    return data


def get_projects_data(projects_model):
    data = pd.DataFrame(list(projects_model.objects.all().values()))
    data = homologate_field(data, u'IdUsuario')
    data = homologate_field(data, u'IdProyecto')
    return data


def format_projects_data(data):

    data = get_year_and_month(data, u'FechaInicio')
    data[u'Plazo'] = data[u'PlazoDias'] // 30
    data['Duracion'] = (
        (pd.to_datetime(data[u'FechaTermino'], errors='coerce') -
         data[u'FechaInicio']) / np.timedelta64(1, 'D')).apply(np.ceil)

    return data


def get_users_data(user_model):
    data = pd.DataFrame(list(user_model.objects.all().values()))
    return homologate_field(data, u'IdUsuario') if not data.empty else data


def format_users_data(data):
    CP = get_CP()
    data['EstadoCivil'] = data['EstadoCivil'].fillna('ND')
    data['Genero'] = data['Genero'].fillna('ND')

    data.loc[data[u'EstadoCivil'] == '', u'EstadoCivil'] = 'ND'
    data.loc[data[u'Genero'] == '', u'Genero'] = 'ND'

    return pd.merge(data, CP, how='left', on=[u'CodigoPostal'])


def get_fundind_data(funding_model):
    data = pd.DataFrame(list(funding_model.objects.all().values()))
    data = homologate_field(data, u'IdUsuario')
    return homologate_field(data, u'IdProyecto')


def format_funding_data(data):
    return get_year_and_month(data, u'Fecha')


def merge_data(projects_data, users_data, fundings_data):
    projects_users_data = pd.merge(
        projects_data,
        users_data[[u'IdUsuario', u'Genero', 'cve', 'EstadoCivil']],
        how='left',
        on=[u'IdUsuario'])

    success = fundings_data[[u'IdProyecto', u'ExitoFondeo']].drop_duplicates()
    projects_users_data = pd.merge(
        projects_users_data, success, how='left', on=[u'IdProyecto'])

    projects_users_data[u'ExitoFondeo'] = projects_users_data[
        u'ExitoFondeo'].fillna(False)
    projects_users_data[u'ExitoFondeo'] = projects_users_data.apply(
        lambda x: int(x[u'ExitoFondeo']) if x[u'ExitoFondeo'] else int(x[u'MontoRecaudado'] >= x[u'MontoPedido']),
        axis=1)

    fundings_users_data = pd.merge(
        fundings_data,
        users_data[[u'IdUsuario', u'Genero', 'cve', 'EstadoCivil']],
        how='left',
        on=[u'IdUsuario'])
    return projects_users_data, fundings_users_data


def get_indexes(indexes, _id, estatal=False):
    data = pd.concat([
        get_index_data(_id="%s%s" % (_id, i + 1), **idx)
        for i, idx in enumerate(indexes)
    ])
    data[u'cve'] = 0
    if estatal:
        estatal = pd.concat([
            get_index_data(_id="%s%s" % (_id, i + 1), estatal=True, **idx)
            for i, idx in enumerate(indexes)
        ])
        data = pd.concat([data, estatal])

    ID2 = get_ids2(data)
    data = pd.merge(data, ID2, how='left', on=[u'id3', u'id'])

    del data['id3']
    data[u'DesGeo'] = data[u'cve'].map(lambda x: 'N' if x == 0 else 'E')
    DesGeo = data[['id', 'DesGeo']].drop_duplicates()
    RangeT = data[['id', 't', 'm']].drop_duplicates().rename(
        columns={"t": "ranget",
                 "m": "rangem"})
    return data, ID2, DesGeo, RangeT


def get_acumulado(data, name):
    years = data['t'].drop_duplicates().values
    file_acumulado = []
    acumulado = []
    for y in range(min(years), max(years) + 1):
        by_year = data.loc[data["t"] == y]
        quarters = by_year['m'].drop_duplicates().values
        quarters.sort()
        for q in quarters:
            by_quarter = by_year.loc[by_year["m"] == q]
            actual = by_quarter[[u'id', u'cve', 'id2', 'valor', 'DesGeo']]

            acumulado.append(actual)

            aux = pd.concat(acumulado).groupby(
                [u'id', u'cve', 'id2', 'DesGeo'])['valor'].sum().reset_index(
                    name="valor")
            aux["t"] = y
            aux["m"] = q
            aux["id"] = aux["id"].astype(str) + "1"

            file_acumulado.append(aux)
    path = '%s%s' % (DATA_PATH, name)

    pd.concat(file_acumulado).to_csv(
        '%sAcumulado.csv' % path, index=False, columns=FORMAT)


def save_data(name, data, ID2, DesGeo, RangeT):
    path = '%s%s' % (DATA_PATH, name)
    data.to_csv('%s.csv' % path, index=False, columns=FORMAT)
    ID2.to_csv('%sCodigosGrupos.csv' % path, index=False)
    DesGeo.to_csv('%sDesGeo.csv' % path, index=False)
    RangeT.to_csv('%sRangosTemporales.csv' % path, index=False)
