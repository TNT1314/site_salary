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

from django.db.utils import IntegrityError
from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from website.models.employee_info import EmployeeInfo
from webapi.serializers.ser_employee import (
    S_Employee, S_L_Employee, S_CN_Employee
)


def user_get_employees_pager(user, p_size, p_numb, name, phone, sortdatafield, sortorder):
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

        query['company'] = user.company

        sortdatafield = sortdatafield if sortdatafield else "add_time"

        sortorder = sortorder if sortorder else "desc"

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


def user_get_employee_by_id(user, id):
    """
        根据ID获取人员信息
    """
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    s_employee = None
    m_employee = EmployeeInfo.objects.filter(company=user.company, id=id)

    if m_employee.first():
        s_employee = S_Employee(m_employee.first())

    results = s_employee.data if s_employee else None
    return code, mess, results


def user_add_employee(user, name, phone, gender, email, status, address):
    """
        用户添加公司用户
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    try:
        n_employee = EmployeeInfo()
        n_employee.company = user.company
        n_employee.name = name
        n_employee.phone = phone
        n_employee.gender = gender
        n_employee.email = email
        n_employee.status = status
        n_employee.address = address
        n_employee.save()

        data['id'] = n_employee.id
        data['name'] = n_employee.name
    except IntegrityError:
        code = ApiCode.edilineerror.code
        mess = u"请不要多次添加同一人！"
    return code, mess, data


def user_update_employee(user, id, name, phone, gender, email, status, address):
    """
        用户添加公司用户
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    q_employee = EmployeeInfo.objects.filter(company=user.company, id=id)

    if q_employee.first():
        try:
            m_employee = q_employee.first()
            m_employee.name = name
            m_employee.phone = phone
            m_employee.gender = gender
            m_employee.email = email
            m_employee.status = status
            m_employee.address = address

            m_employee.save()
            data['id'] = m_employee.id
            data['name'] = m_employee.name
        except IntegrityError:
            code = ApiCode.edilineerror.code
            mess = u"请不要多次添加同一人！"
    else:
        code = ApiCode.linenoexists.code
        mess = ApiCode.linenoexists.mess
    return code, mess, data


def user_get_employee_by_term(user, term):
    """
        根据条件模糊查询人员信息
    """
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    query = dict()
    query['name__contains'] = term
    query['company'] = user.company

    m_employee = EmployeeInfo.objects.filter(**query)

    s_employee = S_CN_Employee(m_employee, many=True)
    results = s_employee.data if s_employee else list()

    return code, mess, results
