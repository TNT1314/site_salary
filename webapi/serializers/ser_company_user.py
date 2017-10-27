#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-27
    desc: 
        site_salary
"""

from rest_framework import serializers
from website.models.company_user import CompanyUser


class S_P_CompanyUser(serializers.ModelSerializer):
    """
        用户列表序列化
    """

    is_staff = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = CompanyUser
        fields = [
            "id", "username", "name",
            "is_staff", "is_active", "address",
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

    def get_address(self, obj):
        """
            用户公司地址
            :param obj:
            :return:
        """
        return obj.company.address if obj.company else u"暂无公司或暂无公司地址"