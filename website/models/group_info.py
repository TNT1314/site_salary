#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/10/30 22:02
    @description:
        权限分组
    
"""

__all__ = ['GroupInfo']

from django.db import models
from .base_model import ModelsBase


class GroupInfo(ModelsBase):
    """
        分组信息
    """

    code = models.CharField('分组编码', unique=True, max_length=10, null=True, blank=True)
    name = models.CharField('分组名称', max_length=10, null=False, blank=False)
    desc = models.CharField('分组描述', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'group_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = "分组信息"

    def __unicode__(self):
        return u"{}({})".format(self.name, self.code)