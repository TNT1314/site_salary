#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/11/2 00:05
    @description:
        企业员工业务类
"""

from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from website.models.employee_info import EmployeeInfo
from webapi.serializers.ser_employee import S_L_Employee

def get_employees_pager(p_size, p_numb, name, phone, sortdatafield, sortorder):
    """

        :param p_size:
        :param p_num:
        :return:
    """

    query = dict()
    results = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        if name:
            query['name__contains'] = name

        if phone:
            query['phone'] = phone

        sortdatafield = sortdatafield if sortdatafield else "id"

        sortorder = sortorder if sortorder else "asc"

        start, end = get_paging_index(p_size, p_numb)

        if sortorder == 'asc':
            m_query = EmployeeInfo.objects.filter(**query).order_by(sortdatafield)
        else:
            m_query = EmployeeInfo.objects.filter(**query).order_by("-{}".format(sortdatafield))

        results['TotalRows'] = m_query.count()

        s_employees = S_L_Employee(m_query[start:end], many=True)

        results['DataRows'] = list()

        results['DataRows'] = s_employees.data
    except Exception as e:
        code = ApiCode.unkonwnerror.code
        mess = e.message
    return code, mess, results
