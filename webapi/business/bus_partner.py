#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-13
    desc: 
        site_salary
"""


from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index, chinese2pinyin
from site_salary.common.split_ch import check_contain_chinese

from website.models.partner_info import PartnerInfo
from webapi.serializers.ser_partner import (
    S_A_Partner, S_Page_Partner, S_Term_Partner
)


def user_get_partners_pager(user, p_size, p_numb, q_code, q_name, sort_field, sort_order):
    """
        用户获取企业合作伙伴分页方法
    """

    query = dict()
    results = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        if q_code:
            query['name__contains'] = q_code
        if q_name:
            query['name__contains'] = q_name

        query['company'] = user.company
        sort_field = sort_field if sort_field else "add_time"
        sort_order = sort_order if sort_order else "desc"
        start, end = get_paging_index(p_size, p_numb)
        if sort_order == 'asc':
            m_query = PartnerInfo.objects.filter(**query).order_by(sort_field)
        else:
            m_query = PartnerInfo.objects.filter(**query).order_by("-{}".format(sort_field))
        results['TotalRows'] = m_query.count()
        s_employees = S_Page_Partner(m_query[start:end], many=True)
        results['DataRows'] = list()
        results['DataRows'] = s_employees.data
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, results


def user_add_partner(user, name, short_name, supplier, customer, phone, society_code,
                link_man, link_man_phone, send_man, send_man_phone, address):
    """
        添加伙伴
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess
    pinyin = chinese2pinyin(name)

    q_query = PartnerInfo.objects.filter(code=pinyin, company=user.company)

    if q_query.first():
        code = ApiCode.repeatserror.code
        mess = u"请不要提交相同名字的伙伴信息"
    else:
        m_object = PartnerInfo()
        m_object.code = pinyin
        m_object.name = name
        m_object.company = user.company
        m_object.short_name = short_name
        m_object.supplier = supplier if supplier else False
        m_object.customer = customer if customer else False
        m_object.phone = phone
        m_object.address = address
        m_object.society_code = society_code
        m_object.link_man = link_man
        m_object.link_man_phone = link_man_phone
        m_object.send_man = send_man
        m_object.send_man_phone = send_man_phone
        m_object.add_com_user = user
        m_object.save()
        data['id'] = m_object.id
    return code, mess, data


def user_change_partner(user, id, name, short_name, supplier, customer, phone, society_code,
                link_man, link_man_phone, send_man, send_man_phone, address):
    """
        修改伙伴信息
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess
    pinyin = chinese2pinyin(name)

    q_query = PartnerInfo.objects.filter(code=pinyin, company=user.company).exclude(id=id)

    if q_query.first():
        code = ApiCode.repeatserror.code
        mess = u"请不要提交相同名字的伙伴信息"
    else:
        m_objects = PartnerInfo.objects.filter(id=id, company=user.company)
        m_object = m_objects.first()
        if m_object:
            m_object.code = pinyin
            m_object.name = name
            m_object.company = user.company
            m_object.short_name = short_name
            m_object.supplier = supplier if supplier else False
            m_object.customer = customer if customer else False
            m_object.phone = phone
            m_object.address = address
            m_object.society_code = society_code
            m_object.link_man = link_man
            m_object.link_man_phone = link_man_phone
            m_object.send_man = send_man
            m_object.send_man_phone = send_man_phone
            m_object.cha_com_user = user
            m_object.save()
            data['id'] = m_object.id
        else:
            code = ApiCode.linenoexists.code
            mess = u"请求的数据不存在，请核实"
    return code, mess, data


def user_get_partner_by_id(user, id):
    """
        用户获取企业合作伙伴分页方法
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess
    m_querys = PartnerInfo.objects.filter(company=user.company,id=id)
    m_query = m_querys.first()
    if m_query:
        s_objects = S_A_Partner(m_query)
        data = s_objects.data
    else:
        code = ApiCode.linenoexists.code
        mess = u"请求的数据不存在，请核实"
    return code, mess, data


def get_partner_by_term(user, term):
    """
        用户获取企业合作伙伴分页方法
    """

    data = list()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    query = dict()
    query['company'] = user.company
    if check_contain_chinese(term):
        query['name__contains'] = term
    else:
        query['code__contains'] = term.lower()
    m_query = PartnerInfo.objects.filter(**query)

    if m_query:
        ser_obj = S_Term_Partner(m_query, many=True)
        data = ser_obj.data
    else:
        code = ApiCode.linenoexists.code
        mess = u"请求的数据不存在，请核实"

    return code, mess, data