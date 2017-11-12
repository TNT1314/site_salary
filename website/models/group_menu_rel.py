#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/10/30 22:03
    @description:
    
    
"""
__all__ = ['GroupMenuRel']

from django.db import models
from .base_model import ModelsBase


class GroupMenuRel(ModelsBase):
    """
        分组信息
    """

    group =  models.ForeignKey('GroupInfo', null=False, blank=False, db_constraint=False,
                               verbose_name='分组信息', on_delete=models.DO_NOTHING, db_index=True, help_text='分组信息')
    menu = models.ForeignKey('MenuInfo', null=False, blank=False, db_constraint=False,
                             verbose_name='菜单信息', on_delete=models.DO_NOTHING, db_index=True, help_text='菜单信息')
    p_inf = models.BooleanField('查询权限', default=False, null=False, blank=False)
    p_add = models.BooleanField('添加权限', default=False, null=False, blank=False)
    p_cha = models.BooleanField('修改权限', default=False, null=False, blank=False)
    p_aud = models.BooleanField('审核权限', default=False, null=False, blank=False)
    p_del = models.BooleanField('删除权限', default=False, null=False, blank=False)
    p_pri = models.BooleanField('打印权限', default=False, null=False, blank=False)

    class Meta:
        db_table = 'group_menu_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = "分组权限"

    def __unicode__(self):
        return u"{}({})".format(self.group.name, self.menu.name)