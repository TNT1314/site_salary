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


__all__ = ['QuarterSalary']


from django.db import models
from .base_model import ModelsBase
from site_salary.common.define import (
    ENUM_QUARTER_ALL, LIST_QUARTER_ALL,
    ENUM_STATUS_ALL, LIST_STATUS_ALL
)


class QuarterSalary(ModelsBase):
    """
        季度工资表
    """

    year = models.CharField("年度", null=False, blank=False, max_length=4, db_index=True, help_text="工资发生的年份")
    quarter = models.IntegerField("季度", null=False, blank=False,choices=LIST_QUARTER_ALL, default=ENUM_QUARTER_ALL.ONE,db_index=True, help_text="工资发生的季度")
    employee = models.ForeignKey('EmployeeInfo', null=False, blank=False, db_constraint=False, verbose_name='雇员', on_delete=models.DO_NOTHING, db_index=True, help_text='该工资单的雇员')
    company = models.ForeignKey('CompanyInfo', null=False, blank=False, db_constraint=False, verbose_name='公司', on_delete=models.DO_NOTHING, db_index=True, help_text='公司')
    count = models.IntegerField("工件数量", null=False, blank=False, default=0, help_text='当前季度的总额')
    salary = models.DecimalField("工资总额", null=False, blank=False, max_digits=16, decimal_places=2, default=0.00, help_text='当前季度的总额')
    status = models.IntegerField("状态", choices=LIST_STATUS_ALL, default=ENUM_STATUS_ALL.NEW, null=False, blank=False, help_text="工资单状态")

    class Meta:
        db_table = 'quarter_salary'
        app_label = 'website'
        verbose_name = verbose_name_plural = '季度工资表'
        unique_together = ('year', 'quarter', 'employee', 'company')

    def __unicode__(self):
        return u"{}({}{})".format(self.employee.name, self.year, self.quarter)


class QuarterSalaryItem(ModelsBase):
    """
        季度工资明细
    """

    parent = models.ForeignKey('QuarterSalary', null=False, blank=False, db_constraint=False, verbose_name='工资主表', related_name='items', on_delete=models.CASCADE, db_index=True, help_text='工资主表')
    process = models.ForeignKey('ProcessPrice', null=False, blank=False, db_constraint=False, verbose_name='工件定价', on_delete=models.DO_NOTHING, db_index=True, help_text='加工工件定价ID')
    material = models.ForeignKey('MaterialInfo', null=False, blank=False, db_constraint=False, verbose_name='工件', on_delete=models.DO_NOTHING, db_index=True, help_text='加工工件')
    mat_name = models.CharField("工件名称", null=False, blank=False, max_length=100, db_index=True, help_text="工件名称")
    mat_standards = models.CharField('工件规格', max_length=500, null=True, blank=True, help_text="物料规格，从长宽高等汇总")
    mat_price = models.DecimalField("加工价格", null=False, blank=False, max_digits=16, decimal_places=2, default=0.00, help_text='加工该物料的价格')
    mat_count = models.IntegerField("计件数量", null=False, blank=False, default=0, help_text='加工该物料的价格')
    mat_unit = models.CharField("计件单位", max_length=100, null=False, blank=False, default="件", help_text='计件单位')
    mat_total = models.DecimalField("计件金额", null=False, blank=False, max_digits=16, decimal_places=2, default=0.00, help_text='计件金额， 加工价格*计件数量')

    class Meta:
        db_table = 'quarter_salary_item'
        app_label = 'website'
        verbose_name = verbose_name_plural = '季度工资明细表'
        ordering = ['mat_name', 'mat_standards']

    def __unicode__(self):
        return u"{}({})".format(self.mat_name, self.mat_standards)