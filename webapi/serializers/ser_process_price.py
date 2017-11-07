#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-07
    desc: 
        site_salary
"""


from rest_framework import serializers
from website.models.process_price import ProcessPrice


class S_ProcessPrice(serializers.ModelSerializer):
    """
        物料加工定价
    """

    class Meta:
        model = ProcessPrice
        fields = "__all__"


class S_L_ProcessPrice(serializers.ModelSerializer):
    """
        企业物料列表序列化
    """

    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    help = serializers.SerializerMethodField()
    standards = serializers.SerializerMethodField()

    add_time = serializers.SerializerMethodField()
    cha_time = serializers.SerializerMethodField()

    class Meta:
        model = ProcessPrice
        fields = [
            "id", "code", "name", "help", "standards", "price", "unit", "add_time", "cha_time"
        ]

    def get_code(self, obj):
        """
            获取code
            :param obj:
            :return:
        """
        return obj.material.code

    def get_name(self, obj):
        """
            获取code
            :param obj:
            :return:
        """
        return obj.material.name

    def get_help(self, obj):
        """
            获取help
            :param obj:
            :return:
        """
        return obj.material.help

    def get_standards(self, obj):
        """
            获取standards
            :param obj:
            :return:
        """
        return obj.material.standards

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
 
