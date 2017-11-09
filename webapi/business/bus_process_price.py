#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-07
    desc: 
        site_salary
"""

from django.db import transaction
from django.db.utils import IntegrityError

from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from website.models.process_price import ProcessPrice
from website.models.material_info import MaterialInfo
from webapi.serializers.ser_material import S_Price_MaterialInfo
from webapi.serializers.ser_process_price import (
    S_ProcessPrice, S_L_ProcessPrice,
)


def user_get_process_price_pager(user, p_size, p_numb, sortdatafield, sortorder, q_code, q_name, q_help):
    """
        用户获取物料定价列表
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
            query['material__code__contains'] = q_code
        if q_name:
            query['material__name__contains'] = q_name
        if q_help:
            query['material__help__contains'] = q_help

        query['material__company'] = user.company

        sortdatafield = sortdatafield if sortdatafield else "add_time"

        if sortdatafield not in ['id', 'add_time', 'cha_time', 'price']:
            sortdatafield = "material__{}".format(sortdatafield)

        sortorder = sortorder if sortorder else "desc"

        start, end = get_paging_index(p_size, p_numb)

        if sortorder == 'asc':
            m_query = ProcessPrice.objects.filter(**query).order_by(sortdatafield)
        else:
            m_query = ProcessPrice.objects.filter(**query).order_by("-{}".format(sortdatafield))

        results['TotalRows'] = m_query.count()

        s_serails = S_L_ProcessPrice(m_query[start:end], many=True)

        results['DataRows'] = list()

        results['DataRows'] = s_serails.data
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, results


def user_get_process_price(user, id):
    """
        用户根据ID获取物料定价信息
        :param user:
        :param id:
        :return:
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess
    q_sets = ProcessPrice.objects.filter(material__company=user.company, id=id)

    q_object = q_sets.first()
    q_material = q_object.material
    s_serial = S_ProcessPrice(q_object) if q_object else None
    s_price_serial = S_Price_MaterialInfo(q_material) if q_material else None
    s_price_data = s_price_serial.data if s_price_serial else None
    data = s_serial.data if s_serial else None
    del data['material']
    if s_price_data:
        data.update(s_price_data)
    return code, mess, data


def user_add_process_price(
                user, name, price, unit, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit):
    """
        用户添加物料及物料价格信息
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        with transaction.atomic():
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

            m_price = ProcessPrice()
            m_price.material = m_model
            m_price.price = price
            m_price.unit = unit
            m_price.save()

        data['id'] = m_price.id
        data['name'] = m_model.name
        data['price'] = m_price.price
    except IntegrityError:
        code = ApiCode.edilineerror.code
        mess = u"请不要添加一个已经存在的数据！"
    return code, mess, data


def user_update_process_price(
                user, id, name, price, unit, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit):
    """
        用户修改物料定价信息
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    query_set = ProcessPrice.objects.filter(material__company=user.company, id=id)
    m_price = query_set.first()

    if m_price:
        try:
            m_model = m_price.material

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

            m_price.price = price
            m_price.unit = unit
            m_price.save(update_fields=['price', 'unit'])

            data['id'] = m_model.id
            data['name'] = m_model.name
        except IntegrityError:
            code = ApiCode.edilineerror.code
            mess = u"请不要修改当前记录为已存在的数据！"
    else:
        code = ApiCode.linenoexists.code
        mess = ApiCode.linenoexists.mess
    return code, mess, data


def user_get_process_price_simple(user, name):
    """
        用户根据ID获取物料定价信息
        :param user:
        :param id:
        :return:
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess

    query = dict()

    if name:
        query['material__name__contains'] = name

    query['material__company'] = user.company

    q_sets = ProcessPrice.objects.filter(**query)

    s_serial = S_L_ProcessPrice(q_sets, many=True) if q_sets else None

    data = s_serial.data if s_serial else None

    return code, mess, data