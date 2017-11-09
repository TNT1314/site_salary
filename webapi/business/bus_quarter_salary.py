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

import json

from decimal import Decimal
from decimal import getcontext

from django.db import transaction
from django.db.utils import IntegrityError

from site_salary.common.apicode import ApiCode
from site_salary.common.untils import get_paging_index
from website.models.employee_info import EmployeeInfo
from website.models.process_price import ProcessPrice
from website.models.quarter_salary import QuarterSalary, QuarterSalaryItem

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


def user_add_quarter_salary(user, year, employee, quarter, remarks, items):
    """
        添加企业员工季度工资记录
        :param user:
        :param year:
        :param employee:
        :param quarter:
        :param remarks:
        :param items:
        :return:
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    has_employee = EmployeeInfo.objects.filter(company=user.company, id=employee).exists()

    if has_employee:
        process_prices = json.loads(items)

        getcontext().prec = 2

        quarter_salary_count = 0
        quarter_salary_total = Decimal(0.00)

        quarter_salary_items = list()

        for process_price in process_prices:
            m_process_price = ProcessPrice.objects.get(pk=process_price['material'])

            quarter_salary_item = QuarterSalaryItem()
            quarter_salary_item.material = m_process_price.material
            quarter_salary_item.mat_name = m_process_price.material.name
            quarter_salary_item.mat_standards = m_process_price.material.standards
            quarter_salary_item.mat_unit = m_process_price.unit
            quarter_salary_item.mat_count = int(process_price['mat_count'])
            quarter_salary_item.mat_price = Decimal(process_price['mat_price'])
            quarter_salary_item.mat_total = Decimal(process_price['mat_price']) * Decimal(process_price['mat_count'])
            quarter_salary_item.remarks = process_price['remarks']

            quarter_salary_count += process_price['mat_count']
            quarter_salary_total += quarter_salary_item.mat_total

            quarter_salary_items.append(quarter_salary_item)

        m_quarter_salary = QuarterSalary()
        m_quarter_salary.company = user.company
        m_quarter_salary.year = year
        m_quarter_salary.employee_id = employee
        m_quarter_salary.quarter = quarter
        m_quarter_salary.count = quarter_salary_count
        m_quarter_salary.salary = quarter_salary_total

        try:
            with transaction.atomic():
                m_quarter_salary.save()
                for item in quarter_salary_items:
                    item.parent = m_quarter_salary
                    item.save()

            data['id'] = m_quarter_salary.id
            data['name'] = m_quarter_salary.employee.name
        except IntegrityError:
            code = ApiCode.edilineerror.code
            mess = "请勿为通一个人添加相同季度的工资记录！"
    else:
        code = ApiCode.linenoexists.code
        mess = ApiCode.linenoexists.mess

    return code, mess, data