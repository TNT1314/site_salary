#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-15
    desc: 
        site_salary
"""

import json
from datetime import datetime

from django.db import transaction

from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from site_salary.common.define import ENUM_PACK_STATUS

from website.models.material_info import MaterialInfo
from website.models.pact_price import PactPrice,PactPriceItem
from webapi.serializers.ser_pact_price import (
    S_Page_PactPrice, S_Item_PactPrice
)


def get_pact_price_pager(user, pagesize, pagenum, partner, partner_code, sort_field, sort_order):
    """
        获取定价协议分页列表
    """

    query = dict()
    results = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        if partner:
            query['id'] = partner
        if partner_code:
            query['partner_code__contains'] = partner_code

        query['company'] = user.company
        sort_field = sort_field if sort_field else "add_time"
        sort_order = sort_order if sort_order else "desc"
        start, end = get_paging_index(pagesize, pagenum)
        if sort_order == 'asc':
            m_query = PactPrice.objects.filter(**query).order_by(sort_field)
        else:
            m_query = PactPrice.objects.filter(**query).order_by("-{}".format(sort_field))
        results['TotalRows'] = m_query.count()
        s_employees = S_Page_PactPrice(m_query[start:end], many=True)
        results['DataRows'] = list()
        results['DataRows'] = s_employees.data
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, results


def get_pact_price_by_id(user, id):
    """
        获取定价协议明细
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        q_objects = PactPrice.objects.filter(company=user.company, id=id)
        m_object = q_objects.first()
        if m_object:
            s_object = S_Item_PactPrice(m_object)
            data = s_object.data
        else:
            code = ApiCode.linenoexists.code
            mess = ApiCode.linenoexists.mess
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, data


def validate_pact_price_item(company, items):
    """
        验证协议明细
    """
    validate = ApiCode.success.code
    validate_mess = u'验证通过'
    validate_result = list()

    try:
        items = json.loads(items)

        for item in items:
            material_id = item.get('material_id')
            if material_id:
                material_objs = MaterialInfo.objects.filter(id=material_id,company=company)
                if material_objs.first():
                    obj_item = PactPriceItem()
                    obj_item.material_id = material_objs.first()
                    obj_item.material_unit = item.get('material_unit')
                    obj_item.process_price = item.get('process_price')
                    obj_item.loss_price = item.get('loss_price')
                    obj_item.remarks = item.get('remarks')
                    validate_result.append(obj_item)
                else:
                    validate = ApiCode.edilineerror.code
                    validate_mess = u'物料数据不存在！'
                    break
            else:
                validate = ApiCode.edilineerror.code
                validate_mess = u'物料信息不能为空！'
                break
    except Exception as e:
        validate = ApiCode.edilineerror.code
        validate_mess = e.message
        validate_result = list()
    return validate, validate_mess, validate_result


def add_pact_price(
        user, pact_type, partner, partner_code,
        send_man, send_man_phone, send_address, remarks, items):
    """
        添加定价协议
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    # 验证唯一
    q_objects = PactPrice.objects.filter(
        company=user.company, pact_type=pact_type, partner_id=partner,
        partner_code=partner_code
    )

    if q_objects.first():
        code = ApiCode.repeatserror.code
        mess = u"请勿为同一个伙伴的同一个合同添加定价协议"
    else:
        valid, valid_mess, valid_list = validate_pact_price_item(user.company, items)
        if valid == code:
            pact_price_obj = PactPrice()
            pact_price_obj.company = user.company
            pact_price_obj.pact_code = 'XY-{}-{:0>4}-{}'.format(
                pact_type, partner, partner_code
            )
            pact_price_obj.partner_id = partner
            pact_price_obj.status = ENUM_PACK_STATUS.XZ
            pact_price_obj.partner_code = partner_code
            pact_price_obj.send_man = send_man
            pact_price_obj.send_man_phone = send_man_phone
            pact_price_obj.send_address = send_address
            pact_price_obj.add_com_user = user
            pact_price_obj.remarks = remarks

            with transaction.atomic():
                pact_price_obj.save()
                for valid_obj in valid_list:
                    valid_obj.parent = pact_price_obj.id
                    valid_obj.save()

            mess = u'提交成功！'
            s_obj = S_Item_PactPrice(pact_price_obj)
            data = s_obj.data
        else:
            code, mess = valid, valid_mess
    return code, mess, data


def cha_pact_price(
        user, id, pact_type, partner, partner_code,
        send_man, send_man_phone, send_address, remarks, items):
    """
        添加定价协议
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    # 验证唯一
    q_objects = PactPrice.objects.filter(
        company=user.company, pact_type=pact_type, partner_id=partner,
        partner_code=partner_code
    ).exclude(id=id)

    if q_objects.first():
        code = ApiCode.repeatserror.code
        mess = u"请勿为同一个伙伴的同一个合同添加定价协议"
    else:
        valid, valid_mess, valid_list = validate_pact_price_item(user.company, items)
        if valid == code:
            pact_price_obj = PactPrice.objects.get(pk=id)
            pact_price_obj.company = user.company
            pact_price_obj.pact_code = 'XY-{}-{:0>4}-{}'.format(
                pact_type, partner, partner_code
            )
            pact_price_obj.partner_id = partner
            pact_price_obj.status = ENUM_PACK_STATUS.XZ
            pact_price_obj.partner_code = partner_code
            pact_price_obj.send_man = send_man
            pact_price_obj.send_man_phone = send_man_phone
            pact_price_obj.send_address = send_address
            pact_price_obj.add_com_user = user

            with transaction.atomic():
                # 删除原单据明细
                items_old = PactPriceItem.objects.filter(parent__id=pact_price_obj.id)

                for item_old in items_old:
                    item_old.delete()

                pact_price_obj.save()
                for valid_obj in valid_list:
                    valid_obj.parent = pact_price_obj.id
                    valid_obj.save()

            mess = u'修改成功！'
            s_obj = S_Item_PactPrice(pact_price_obj)
            data = s_obj.data
        else:
            code, mess = valid, valid_mess
    return code, mess, data


def audit_pact_price(user, id):
    """
        审核定价协议
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    # 验证唯一
    q_objects = PactPrice.objects.filter(company=user.company, id=id)

    if q_objects.first():
        q_object = q_objects.first()

        q_object.status = ENUM_PACK_STATUS.SH
        q_object.aud_user = user
        q_object.aud_time = datetime.now()

        q_object.save(update_fileds=['status', 'aud_user', 'aud_time'])

        s_obj = S_Item_PactPrice(q_object)
        data = s_obj.data
    else:
        code = ApiCode.recordserror.code
        mess = ApiCode.recordserror.mess
    return code, mess, data


def delete_pact_price(user, id):
    """
        删除定价协议
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    # 验证唯一
    q_objects = PactPrice.objects.filter(company=user.company, id=id)

    if q_objects.first():
        q_object = q_objects.first()

        q_object.status = ENUM_PACK_STATUS.JY
        q_object.del_user = user
        q_object.del_time = datetime.now()

        q_object.save(update_fileds=['status', 'del_user', 'del_time'])

        s_obj = S_Item_PactPrice(q_object)
        data = s_obj.data
    else:
        code = ApiCode.recordserror.code
        mess = ApiCode.recordserror.mess
    return code, mess, data