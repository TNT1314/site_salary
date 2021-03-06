#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-23
    desc: 
        site_salary
"""

from django.contrib.auth.models import User

from site_salary.common.untils import get_paging_index

from webapi.serializers.ser_user import S_L_User


def get_users_by_name(username):
    """
        :param p_size:
        :param p_num:
        :return:
    """

    results = dict()

    query = dict()

    if username:
        query['username__contains'] = username

    obj_user = User.objects.filter(**query).order_by("username")

    ser_user = S_L_User(obj_user, many=True)

    results['DataRows'] = ser_user.data

    return results


def get_users_by_params(p_size, p_numb, username, email, sortdatafield, sortorder):
    """

        :param p_size:
        :param p_num:
        :return:
    """
    results = dict()

    query = dict()

    if username:
        query['username__contains'] = username

    if email:
        query['email__contains'] = email

    sortdatafield = sortdatafield if sortdatafield else "id"

    sortorder = sortorder if sortorder else "asc"

    start, end = get_paging_index(p_size, p_numb)

    if sortorder == 'asc':
        obj_user = User.objects.filter(**query).order_by(sortdatafield)
    else:
        obj_user = User.objects.filter(**query).order_by("-{}".format(sortdatafield))

    results['TotalRows'] = obj_user.count()

    ser_user = S_L_User(obj_user[start:end], many=True)

    results['DataRows'] = list()

    results['DataRows'] = ser_user.data

    return results


def get_user_by_id(id):
    """

    :param id:
    :return:
    """
    result = dict()

    obj_user = User.objects.get(pk=id)

    ser_user = S_L_User(obj_user)

    result['code'] = 0

    result['message'] = u"查询成功!"

    result['json'] = ser_user.data

    return result