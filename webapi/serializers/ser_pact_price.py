#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-15
    desc: 
        site_salary
"""

from .ser_base import SerBase
from rest_framework import serializers
from website.models.pact_price import PactPrice,PactPriceItem

from site_salary.common.define import DICT_PACK_STATUS


class S_A_PactPrice(serializers.ModelSerializer):
    """
        定价协议序列化
    """

    class Meta:
        model = PactPrice
        fields = ["all"]


class S_A_PactPriceItem(serializers.ModelSerializer):
    """
        定价协议明细序列化
    """

    class Meta:
        model = PactPriceItem
        fields = ["all"]


class S_Page_PactPrice(SerBase):
    """
        定价协议分页序列化
    """

    status = serializers.SerializerMethodField()
    partner = serializers.SerializerMethodField()
    aud_time = serializers.SerializerMethodField()
    del_time = serializers.SerializerMethodField()

    class Meta:
        model = PactPrice
        fields = [
            "id", "pact_code", "pact_type", "partner", "status",
            "partner_code", "send_man", "send_man_phone", "send_address",
            "add_time", "cha_time", "aud_time", "del_time"
        ]

    def get_status(self, obj):
        """
            返回定价协议的状态
            :param obj:
            :return:
        """
        return DICT_PACK_STATUS.get(obj.status, u"未知")

    def get_partner(self, obj):
        """
            返回合作伙伴名称
            :param obj:
            :return:
        """
        return obj.partner.name if obj.partner else None

    def get_aud_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.aud_time.strftime("%Y-%m-%d %H:%M:%S") if obj.aud_time else ""

    def get_del_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.del_time.strftime("%Y-%m-%d %H:%M:%S") if obj.del_time else ""


class S_Item_PactPriceItem(SerBase):
    """
        明细序列化
        用途：明细展示
    """

    material_name = serializers.SerializerMethodField()

    class Meta:
        model = PactPriceItem
        fields = [
            "parent", "material", "material_name", "material_unit",
            "process_price", "loss_price", "remarks"
        ]

    def get_material_name(self, obj):
        """
            获取物料名称
            :param obj:
            :return:
        """
        return obj.material.name


class S_Item_PactPrice(SerBase):
    """
        定价协议分页序列化
        用途： 展示明细
    """


    partner = serializers.SerializerMethodField()
    aud_time = serializers.SerializerMethodField()
    items = S_Item_PactPriceItem(many=True, read_only=True)
    del_time = serializers.SerializerMethodField()

    class Meta:
        model = PactPrice
        fields = [
            "pact_code", "pact_type", "partner", "status", "partner_code",
            "send_man", "send_man", "send_address", "remarks",
            "add_time", "cha_time", "aud_time", "del_time",
            "items"
        ]


    def get_partner(self, obj):
        """
            返回合作伙伴名称
            :param obj:
            :return:
        """

        partner_dict = dict()
        if obj.partner:
            partner_dict['id'] = obj.partner.id
            partner_dict['name'] = obj.partner.name

        return partner_dict

    def get_aud_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.aud_time.strftime("%Y-%m-%d %H:%M:%S") if obj.aud_time else ""

    def get_del_time(self, obj):
        """
            格式化时间
            :param obj:
            :return:
        """
        return obj.del_time.strftime("%Y-%m-%d %H:%M:%S") if obj.del_time else ""