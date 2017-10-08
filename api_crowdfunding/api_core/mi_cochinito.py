#!/usr/bin/env python
# -*- coding: utf-8 -*-
import locale
import os
import time
from datetime import datetime

import numpy as np
import pandas as pd
import requests

locale.setlocale(locale.LC_ALL, '')

TOKEN = os.environ.get('TOKEN')

categories_mapping = {'community': 'Comunitarios', 'innovation': 'Inventos'}

genero_mapping = {'Masculino': 'M', 'Femenino': 'F'}


def get_micochinito(field):
    try:
        return requests.get('https://www.micochinito.com/api/%s?api_token=%s' %
                            (field, TOKEN)).json()
    except requests.exceptions.ConnectionError:
        time.sleep(1)
        return get_micochinito(field)


def get_micochinito_projects():
    MC = get_micochinito('projects')
    ids, users, categories, amount_goal, term, date_init, achieved = [], [], [], [], [], [], []
    for i in MC:
        ids.append(i['project_id'])
        users.append(i['owner_id'])
        categories.append(categories_mapping[i['project_category']])
        amount_goal.append(i['amount_goal'])
        term.append(int(i['project_duration'] or 0))
        date_init.append(
            datetime.strptime(i['project_starts_at']['date'],
                              "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d"))
        achieved.append(i['amout_achieved'])

    d = {
        u'IdProyecto': ids,
        u'IdUsuario': users,
        u'Categoria': categories,
        u'MontoPedido': amount_goal,
        u'PlazoDias': term,
        u'FechaInicio': date_init,
        u'MontoRecaudado': achieved
    }
    return pd.DataFrame(
        data=d,
        columns=[
            u'Categoria', u'CuotaComision', u'FechaInicio', u'FechaTermino',
            u'IdProyecto', u'IdUsuario', u'MontoPedido', u'MontoRecaudado',
            u'PlazoDias', u'Subcategoria', u'TasaInteresAnual'
        ])


def get_micochinito_donors():
    MC = get_micochinito('donors')
    users, gender, age = [], [], []
    for i in MC:
        users.append(i['user_id'])
        gender.append(genero_mapping.get(i['user_gender'], np.nan))
        age.append(i.get('user_age'))

    d = {u'IdUsuario': users, u'Genero': gender, u'Edad': age}

    return pd.DataFrame(
        data=d,
        columns=[
            u'IdUsuario', u'Genero', u'FechaNacimiento', u'Estado', u'Edad',
            u'EstadoCivil', 'CodigoPostal'
        ])


def get_micochinito_donations():
    MC = get_micochinito('donations')
    users, amount, dates = [], [], []
    for i in MC:
        if i['status'] == 'paid':
            users.append(i['charge_id'])
            amount.append(i['amount_to_project'])
            dates.append(
                datetime.strptime(i['created_at']['date'],
                                  "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d"))

    d = {u'IdUsuario': users, u'MontoRecaudado': amount, u'Fecha': dates}
    return pd.DataFrame(
        data=d,
        columns=[
            u'ExitoFondeo', u'Fecha', u'Fondeadores', u'IdProyecto',
            u'IdUsuario', u'MontoRecaudado', u'id', u'user_id'
        ])


def create_excel(name):

    writer = pd.ExcelWriter(name)
    get_micochinito_projects().to_excel(writer, 'Proyecto', index=False)
    get_micochinito_donors().to_excel(writer, 'Usuario', index=False)
    get_micochinito_donations().to_excel(writer, 'Fondeo', index=False)
    writer.save()


def get_data():
    return get_micochinito_projects(), get_micochinito_donors(
    ), get_micochinito_donations()


if __name__ == '__main__':
    create_excel('data/Mi Cochinito 2017.xlsx')
