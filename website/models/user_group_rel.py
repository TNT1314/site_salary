#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/10/30 22:47
    @description:
    
    
"""

__all__ = ['UserGroupRel']


from django.db import models
from .base_model import ModelsBase

class UserGroupRel(ModelsBase):
    """
        菜单信息
    """

    com_user = models.ForeignKey('CompanyUser', null=False, blank=False, db_constraint=False,
                                 verbose_name='用户信息', on_delete=models.DO_NOTHING, db_index=True, help_text='用户信息')
    group = models.ForeignKey('GroupInfo', null=False, blank=False, db_constraint=False,
                                 verbose_name='分组信息', on_delete=models.DO_NOTHING, db_index=True, help_text='分组信息')

    class Meta:
        db_table = 'user_group_rel'
        app_label = 'website'
        verbose_name = verbose_name_plural = "人员分组"

    def __unicode__(self):
        return u"{}({})".format(self.com_user.username, self.menu.name)