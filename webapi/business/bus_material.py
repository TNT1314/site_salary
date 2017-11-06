#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-06
    desc: 
        site_salary
        企业物料业务表
"""

from django.db.utils import IntegrityError
from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from website.models.material_info import MaterialInfo
from webapi.serializers.ser_material import (
    S_L_MaterialInfo, S_MaterialInfo
)


def user_get_materials_pager(user, p_size, p_numb, sortdatafield, sortorder, q_code, q_name, q_help):
    """
        用户获取物料列表
        :param p_size:
        :param p_num:
        :return:
    """

    query = dict()
    results = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        if q_code:
            query['code__contains'] = q_code
        if q_name:
            query['name__contains'] = q_name
        if q_help:
            query['help__contains'] = q_help

        query['company'] = user.company

        sortdatafield = sortdatafield if sortdatafield else "add_time"

        sortorder = sortorder if sortorder else "desc"

        start, end = get_paging_index(p_size, p_numb)

        if sortorder == 'asc':
            m_query = MaterialInfo.objects.filter(**query).order_by(sortdatafield)
        else:
            m_query = MaterialInfo.objects.filter(**query).order_by("-{}".format(sortdatafield))

        results['TotalRows'] = m_query.count()

        s_serails = S_L_MaterialInfo(m_query[start:end], many=True)

        results['DataRows'] = list()

        results['DataRows'] = s_serails.data
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, results


def user_get_material(user, id):
    """
        用户根据ID获取物料信息
        :param user:
        :param id:
        :return:
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess
    q_sets = MaterialInfo.objects.filter(company=user.company, id=id)
    s_serial = S_MaterialInfo(q_sets.first()) if q_sets.first() else None
    data = s_serial.data if s_serial else None
    return code, mess, data


def user_add_material(
                user, name, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit):
    """
        用户添加物料信息
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        m_model = MaterialInfo()
        m_model.company = user.company
        m_model.name = name
        m_model.length = length
        m_model.length_unit = length_unit
        m_model.wide = wide
        m_model.wide_unit = wide_unit
        m_model.height = height
        m_model.height_unit = height_unit
        m_model.diam = diam
        m_model.diam_unit = diam_unit
        m_model.bulk = bulk
        m_model.bulk_unit = bulk_unit
        m_model.weight = weight
        m_model.weight_unit = weight_unit
        m_model.save()
        data['id'] = m_model.id
        data['name'] = m_model.name
    except IntegrityError:
        code = ApiCode.edilineerror.code
        mess = u"请不要添加一个已经存在的数据！"
    return code, mess, data


def user_update_material(
                user, id, name, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit):
    """
        用户修改物料信息
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    query_set = MaterialInfo.objects.filter(company=user.company, id=id)

    if query_set.first():
        try:
            m_model = query_set.first()
            m_model.name = name
            m_model.length = length
            m_model.length_unit = length_unit
            m_model.wide = wide
            m_model.wide_unit = wide_unit
            m_model.height = height
            m_model.height_unit = height_unit
            m_model.diam = diam
            m_model.diam_unit = diam_unit
            m_model.bulk = bulk
            m_model.bulk_unit = bulk_unit
            m_model.weight = weight
            m_model.weight_unit = weight_unit
            m_model.save()
            data['id'] = m_model.id
            data['name'] = m_model.name
        except IntegrityError:
            code = ApiCode.edilineerror.code
            mess = u"请不要修改当前记录为已存在的数据！"
    else:
        code = ApiCode.linenoexists.code
        mess = ApiCode.linenoexists.mess
    return code, mess, data