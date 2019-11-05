#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/10/30 21:53
    @description:
        菜单信息表
    
"""


__all__ = ['MenuInfo']

from django.db import models
from .base_model import ModelsBase


class MenuInfo(ModelsBase):
    """
        菜单信息
    """

    code = models.CharField('菜单编码', unique=True, max_length=10, null=True, blank=True)
    name = models.CharField('菜单名称', max_length=10, null=False, blank=False)
    icon = models.CharField('菜单图标', max_length=20, null=False, blank=False)
    model = models.CharField('模型名称', null=True, blank=True, max_length=100)
    parent = models.ForeignKey('MenuInfo', null=True, blank=True, db_constraint=False,
                               verbose_name='父级菜单', on_delete=models.DO_NOTHING, db_index=True, help_text='父级菜单')
    desc = models.CharField('菜单描述', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'menu_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = "菜单信息"

    def __unicode__(self):
        return u"{}({})".format(self.name, self.code)