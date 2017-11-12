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

from rest_framework import serializers
from site_salary.common.define import (
    DICT_STATUS_ALL, DICT_QUARTER_ALL
)
from website.models.quarter_salary import QuarterSalary, QuarterSalaryItem


class S_QuarterSalary(serializers.ModelSerializer):
    """
        季度工资表
    """

    class Meta:
        model = QuarterSalary
        fields = "__all__"


class S_L_QuarterSalary(serializers.ModelSerializer):
    """
        季度工资表
        用途： 列表展示
    """

    employee = serializers.SerializerMethodField()
    quarter = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    status_code = serializers.SerializerMethodField()
    add_time = serializers.SerializerMethodField()
    cha_time = serializers.SerializerMethodField()

    class Meta:
        model = QuarterSalary
        fields = [
            "id", "year", "quarter", "employee",
            "count", "salary", "status", "status_code",
            "add_time", "cha_time"
        ]

    def get_employee(self, obj):
        """

            :param obj:
            :return:
        """
        return obj.employee.name if obj.employee else None

    def get_quarter(self, obj):
        """

            :param obj:
            :return:
        """
        return DICT_QUARTER_ALL[obj.quarter] if obj.quarter else None

    def get_status(self, obj):
        """
            展示当前状态
            :param obj:
            :return:
        """
        return DICT_STATUS_ALL[obj.status] if obj.status else None

    def get_status_code(self, obj):
        """
            展示当前状态
            :param obj:
            :return:
        """
        return obj.status

    def get_add_time(self, obj):
        """
            格式化添加日期
            :param obj:
            :return:
        """
        return obj.add_time.strftime("%Y-%m-%d %H:%M:%S") if obj.add_time else ""

    def get_cha_time(self, obj):
        """
            格式化修改日期
            :param obj:
            :return:
        """
        return obj.cha_time.strftime("%Y-%m-%d %H:%M:%S") if obj.cha_time else ""


class S_I_QuarterSalaryItem(serializers.ModelSerializer):
    """
        季度工资明细表序列化
    """
    class Meta:
        model = QuarterSalaryItem
        fields = [
            "id", "material", "mat_name", "mat_standards", "mat_price",
            "mat_count", "mat_unit", "mat_total", "remarks",
        ]


class S_I_QuarterSalary(serializers.ModelSerializer):
    """
        季度工资明细表
        用途： 列表展示
    """

    company = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()
    salary = serializers.SerializerMethodField()
    items = S_I_QuarterSalaryItem(many=True, read_only=True)
    add_time = serializers.SerializerMethodField()
    cha_time = serializers.SerializerMethodField()

    class Meta:
        model = QuarterSalary
        fields = [
            "id", "year", "quarter", "employee", "company",
            "count", "salary", "status", "items", "remarks",
            "add_time", "cha_time"
        ]

    def get_company(self, obj):
        """

        :param obj:
        :return:
        """
        return obj.company.name

    def get_employee(self, obj):
        """

            :param obj:
            :return:
        """

        employee = dict()
        employee['id'] = obj.employee.id
        employee['name'] = obj.employee.name
        return employee

    def get_salary(self, obj):
        """

        :param obj:
        :return:
        """
        return '{:.2f}'.format(obj.salary)

    def get_add_time(self, obj):
        """
            格式化添加日期
            :param obj:
            :return:
        """
        return obj.add_time.strftime("%Y-%m-%d %H:%M:%S") if obj.add_time else ""

    def get_cha_time(self, obj):
        """
            格式化修改日期
            :param obj:
            :return:
        """
        return obj.cha_time.strftime("%Y-%m-%d %H:%M:%S") if obj.cha_time else ""