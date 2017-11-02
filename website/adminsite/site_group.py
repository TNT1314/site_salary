#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-02
    desc: 
        site_salary
        分组权限后台模块
"""
__all__ = ['SiteMenuInline',]

from django.contrib import admin
from website.models.group_menu_rel import GroupMenuRel


class SiteGroupMenuRel(admin.TabularInline):
    """
        明细项
    """
    model = GroupMenuRel

    fields = (
        'valid', 'menu',  'p_inf', 'p_add', 'p_cha', 'p_aud', 'p_del', 'remarks'
    )


class SiteGroupInfo(admin.ModelAdmin):
    """
        分组信息展示
    """
    inlines = [
        SiteGroupMenuRel,
    ]
    list_display = (
        'code', 'valid', 'name', 'remarks',
        'add_user', 'add_time',
        'cha_user', 'cha_time',
    )

    search_fields = ('valid', 'code', 'name',)






