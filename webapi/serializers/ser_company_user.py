#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-27
    desc: 
        site_salary
        公司用户序列化
"""

from rest_framework import serializers
from website.models.company_user import CompanyUser


class S_P_CompanyUser(serializers.ModelSerializer):
    """
        用户列表序列化
    """

    is_staff = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = CompanyUser
        fields = [
            "id", "username", "name", "mobile", "email", "password", "avatar",
            "is_staff", "is_active", "company_name",
        ]

    def get_is_staff(self, obj):
        """
            是否允许登录后台
            :param obj:
            :return:
        """
        return u"是" if obj.is_staff else u"否"

    def get_is_active(self, obj):
        """
            是否允许登录后台
            :param obj:
            :return:
        """
        return u"正常" if obj.is_active else u"销户"

    def get_password(self, obj):
        """
            密码选项
            :param obj:
            :return:
        """
        return u'**********'

    def get_company_name(self, obj):
        """
            用户公司地址
            :param obj:
            :return:
        """
        return obj.company.name if obj.company else u"暂无公司或暂无公司地址"