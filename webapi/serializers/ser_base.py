#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-13
    desc: 
        site_salary
"""

__all__ = ['SerBase']

from rest_framework import serializers


class SerBase(serializers.ModelSerializer):
    """
        序列化时间基类
    """
    add_time = serializers.SerializerMethodField()
    cha_time = serializers.SerializerMethodField()

    def get_add_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.add_time.strftime("%Y-%m-%d %H:%M:%S") if obj.add_time else ""

    def get_cha_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.cha_time.strftime("%Y-%m-%d %H:%M:%S") if obj.cha_time else ""