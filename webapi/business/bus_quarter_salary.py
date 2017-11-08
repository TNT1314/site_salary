#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-08
    desc: 
        site_salary
"""

from django.db import transaction
from django.db.utils import IntegrityError

from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from website.models.quarter_salary import QuarterSalary
from webapi.serializers.set_quarter_salary import (
    S_L_QuarterSalary, S_I_QuarterSalary
)


def user_get_quarter_salary_pager(user, p_size, p_numb, sortdatafield, sortorder, year, quarter, name):
    """
        用户获取员工工资列表
        :param p_size:
        :param p_num:
        :return:
    """

    query = dict()
    results = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        if year:
            query['year'] = year
        if quarter:
            query['quarter'] = quarter
        if name:
            query['employee__name__contains'] = name

        query['company'] = user.company

        sortdatafield = sortdatafield if sortdatafield else "add_time"

        sortorder = sortorder if sortorder else "desc"

        start, end = get_paging_index(p_size, p_numb)

        if sortorder == 'asc':
            m_query = QuarterSalary.objects.filter(**query).order_by(sortdatafield)
        else:
            m_query = QuarterSalary.objects.filter(**query).order_by("-{}".format(sortdatafield))

        results['TotalRows'] = m_query.count()

        s_serails = S_L_QuarterSalary(m_query[start:end], many=True)

        results['DataRows'] = list()

        results['DataRows'] = s_serails.data
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, results


def user_get_quarter_salary(user, id):
    """
        用户根据ID获取工人
        :param user:
        :param id:
        :return:
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess
    q_sets = QuarterSalary.objects.filter(company=user.company, id=id)
    q_object = q_sets.first()
    s_serial = S_I_QuarterSalary(q_object) if q_object else None
    data = s_serial.data if s_serial else None
    return code, mess, data