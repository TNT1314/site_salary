#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/11/2 00:08
    @description:
        企业用户序列化
"""

__all__ = ["S_Employee", "S_L_Employee"]

from rest_framework import serializers

from site_salary.common.define import (
    DICT_EMPLOYEE_GENDER,DICT_EMPLOYEE_STATUS
)
from website.models.employee_info import EmployeeInfo


class S_Employee(serializers.ModelSerializer):
    """
        企业员工列表序列化
    """

    class Meta:
        model = EmployeeInfo
        fields = '__all__'


class S_L_Employee(serializers.ModelSerializer):
    """
        企业员工列表序列化
    """

    gender = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    add_time = serializers.SerializerMethodField()
    cha_time = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeInfo
        fields = [
            "id", "name", "gender", "email", "phone", "address",
            "status", 'add_time', 'cha_time'
        ]

    def get_gender(self, obj):
        """
            员工性别
            :param obj:
            :return:
        """
        return DICT_EMPLOYEE_GENDER[obj.gender]

    def get_status(self, obj):
        """
            员工状态
            :param obj:
            :return:
        """
        return DICT_EMPLOYEE_STATUS[obj.status]

    def get_add_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.add_time.strftime("%Y-%m-%d %H:%M:%S") if obj.add_time else ""

    def get_cha_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.cha_time.strftime("%Y-%m-%d %H:%M:%S") if obj.cha_time else ""