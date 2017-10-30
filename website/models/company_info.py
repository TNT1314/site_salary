#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        公司模型
"""

__all__ = ['CompanyInfo']


from django.db import models
from .base_model import ModelsBase
 

class CompanyInfo(ModelsBase):
    """
        公司信息表
    """

    code = models.CharField('公司编码', unique=True, max_length=10, null=True, blank=True)
    name = models.CharField('公司名称', max_length=10, null=False, blank=False)
    shot_name = models.CharField('公司简称', max_length=10, null=False, blank=False)
    license = models.CharField('营业执照', null=True, blank=True, max_length=100)
    address = models.CharField('公司地点', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'company_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = "公司信息"

    def __unicode__(self):
        return u"{}({})".format(self.name, self.code)