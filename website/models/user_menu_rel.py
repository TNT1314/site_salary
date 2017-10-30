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
__all__ = ['UserMenuRel']


from django.db import models
from .base_model import ModelsBase

class UserMenuRel(ModelsBase):
    """
        菜单信息
    """

    com_user = models.ForeignKey('CompanyUser', null=False, blank=False, db_constraint=False,
                                 verbose_name='公司用户信息', on_delete=models.DO_NOTHING, db_index=True, help_text='公司用户信息')
    menu = models.ForeignKey('MenuInfo', null=False, blank=False, db_constraint=False,
                                 verbose_name='菜单信息', on_delete=models.DO_NOTHING, db_index=True, help_text='菜单信息')
    p_inf = models.BooleanField('查询权限', default=True, null=False, blank=False)
    p_add = models.BooleanField('添加权限', default=True, null=False, blank=False)
    p_cha = models.BooleanField('修改权限', default=True, null=False, blank=False)
    p_aud = models.BooleanField('审核权限', default=True, null=False, blank=False)
    p_del = models.BooleanField('删除权限', default=True, null=False, blank=False)

    class Meta:
        db_table = 'user_menu_rel'
        app_label = 'website'
        verbose_name = verbose_name_plural = "人员权限"

    def __unicode__(self):
        return u"{}({})".format(self.com_user.username, self.menu.name)