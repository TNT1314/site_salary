#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/11/1 23:23
    @description:
        雇员基础信息表
"""

__all__ = ['EmployeeInfo']

from django.db import models

from .base_model import ModelsBase

from site_salary.common.define import (
    ENUM_EMPLOYEE_GENDER, LIST_EMPLOYEE_GENDER,
    ENUM_EMPLOYEE_STATUS, LIST_EMPLOYEE_STATUS,
)


class EmployeeInfo(ModelsBase):
    """
        公司雇员信息表
    """

    name = models.CharField('姓名', null=False, blank=False, max_length=100, help_text='员工姓名')
    gender = models.IntegerField('性别', null=False, blank=False, choices=LIST_EMPLOYEE_GENDER, default=ENUM_EMPLOYEE_GENDER.MALE, help_text='性别')
    email = models.EmailField('邮箱', null=True, blank=True, help_text='邮箱地址')
    phone = models.BigIntegerField('联系电话', null=True, blank=True, help_text='联系电话')
    status = models.IntegerField('状态', null=False, blank=False, choices=LIST_EMPLOYEE_STATUS, default=ENUM_EMPLOYEE_STATUS.ONLINE, help_text='员工状态')
    address = models.CharField('家庭住址', null=True, blank=True, max_length=500, help_text='家庭住址')
    company = models.ForeignKey('CompanyInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='公司信息', on_delete=models.DO_NOTHING, db_index=True, help_text='所属公司')

    class Meta:
        db_table = 'employee_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = "公司雇员信息"
        unique_together = ("name", "phone", "company")

    def __unicode__(self):
        return u"{}({})".format(self.name, self.phone)