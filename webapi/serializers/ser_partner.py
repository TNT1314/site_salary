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

__all__ = ["S_Employee", "S_L_Employee"]


from rest_framework import serializers
from .ser_base import SerBase
from website.models.partner_info import PartnerInfo


class S_A_Partner(serializers.ModelSerializer):
    """
        企业合作伙伴全字段序列化
    """

    class Meta:
        model = PartnerInfo
        fields = '__all__'


class S_Term_Partner(serializers.ModelSerializer):
    """
        企业合作伙伴联想查询
    """

    name = serializers.SerializerMethodField()

    class Meta:
        model = PartnerInfo
        fields = [
            "id", "code", "name",
        ]

    def get_name(self, obj):
        return obj.short_name if obj.short_name else obj.name[:10]

class S_Page_Partner(SerBase):
    """
        企业合作伙伴全字段序列化
    """

    supplier = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()

    class Meta:
        model = PartnerInfo
        fields = [
            "id", "code", "name", "short_name", "supplier", "customer", "phone",
            "address", 'add_time', 'cha_time'
        ]

    def get_supplier(self, obj):
        """
            :param obj:
            :return:
        """
        return u"是" if obj.supplier else u""

    def get_customer(self, obj):
        """
            :param obj:
            :return:
        """
        return u"是" if obj.customer else u""