#! usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

"""
    User 序列化文件，不同接口使用不同序列化
"""


from rest_framework import serializers
from django.contrib.auth.models import User


class S_L_User(serializers.ModelSerializer):

    """
        用户列表序列化
    """

    last_login = serializers.SerializerMethodField()
    is_staff = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    is_superuser = serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", "last_login", "username", "email",
            "is_staff", "is_active", "is_superuser", "date_joined",
        ]

    def get_last_login(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.last_login.strftime("%Y-%m-%d %H:%M:%S") if obj.last_login else ""


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

    def get_is_superuser(self, obj):
        """
            超级用户
            :param obj:
            :return:
        """
        return u"超级用户" if obj.is_superuser else u"普通用户"
 
    def get_date_joined(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.date_joined.strftime("%Y-%m-%d %H:%M:%S") if obj.date_joined else ""
