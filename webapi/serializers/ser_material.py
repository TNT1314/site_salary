#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-06
    desc: 
        site_salary
"""

__all__ = ["S_Employee", "S_L_Employee"]


from rest_framework import serializers

from website.models.material_info import MaterialInfo


class S_MaterialInfo(serializers.ModelSerializer):
    """
        企业物料列表序列化
    """

    class Meta:
        model = MaterialInfo
        fields = '__all__'


class S_L_MaterialInfo(serializers.ModelSerializer):
    """
        企业物料列表序列化
    """

    add_time = serializers.SerializerMethodField()
    cha_time = serializers.SerializerMethodField()

    class Meta:
        model = MaterialInfo
        fields = [
            "id", "code", "name", "help", "standards", "add_time", 'cha_time'
        ]

    def get_add_time(self, obj):
        """
            格式化添加日期
            :param obj:
            :return:
        """
        return obj.add_time.strftime("%Y-%m-%d %H:%M:%S") if obj.add_time else ""

    def get_cha_time(self, obj):
        """
            格式化修改日期
            :param obj:
            :return:
        """
        return obj.cha_time.strftime("%Y-%m-%d %H:%M:%S") if obj.cha_time else ""
