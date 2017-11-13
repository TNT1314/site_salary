#! usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/10/30 23:43
    @description:
        权限序列化
"""

from rest_framework import serializers
from website.models.menu_info import MenuInfo


class S_Menu(serializers.ModelSerializer):
    """
        菜单序列化
    """

    class Meta:
        model = MenuInfo
        fields = ["all"]

class S_U_Menu(serializers.ModelSerializer):
    """
        用户权限序列化
    """

    class Meta:
        model = MenuInfo
        fields = [
            "id", "code", "name", "icon", "model", "desc",
        ]