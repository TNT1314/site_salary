#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-14
    desc: 
        site_salary
        协议定价
"""

from django.db import models

from site_salary.common.define import LIST_PACT_TYPE, ENUM_PACT_TYPE, LIST_PACK_STATUS, ENUM_PACK_STATUS
from .base_model_com import ModelsBase


class PactPrice(ModelsBase):
    """
        协议定价
    """

    pact_code = models.CharField('协议编号', unique=True, max_length=50, null=True, blank=True, help_text="该协议的编号")
    pact_type = models.CharField('协议类型', choices=LIST_PACT_TYPE , default=ENUM_PACT_TYPE.JG, max_length=10, null=True, blank=True, help_text="协议类型")
    company = models.ForeignKey('CompanyInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='公司信息', on_delete=models.DO_NOTHING, db_index=True, help_text='对应公司')
    partner = models.ForeignKey('PartnerInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='伙伴信息', on_delete=models.DO_NOTHING, db_index=True, help_text='该合同对应的伙伴')
    partner_code = models.CharField('伙伴协议编号', max_length=100, null=False, blank=False, help_text="该合作伙伴的协议编号")

    status = models.CharField('协议状态', choices=LIST_PACK_STATUS, default=ENUM_PACK_STATUS.XZ, max_length=4, null=True, blank=False, help_text="该协议的状态")

    send_man = models.CharField("收货人", max_length=34, null=True, blank=True, default=None, help_text="该协议规定收货人")
    send_man_phone = models.CharField("收货人电话", max_length=34, null=True, blank=True, default=None,
                                      help_text="该协议规定收货人电话")
    send_address = models.CharField('送货地址', max_length=500, null=True, blank=True, help_text="该协议规定的送货地址")
    aud_user = models.ForeignKey("CompanyUser", default=None,
            editable=False, null=True, blank=True, on_delete=models.DO_NOTHING,
            related_name='aud_user', db_constraint=False, verbose_name='创建人员', db_index=True)
    aud_time = models.DateTimeField("审核时间", null=True, blank=True, help_text="协议的审核时间")
    del_user = models.ForeignKey("CompanyUser", default=None,
                                 editable=False, null=True, blank=True, on_delete=models.DO_NOTHING,
                                 related_name='del_user', db_constraint=False, verbose_name='创建人员', db_index=True)
    del_time = models.DateTimeField("审核时间", null=True, blank=True, help_text="协议的审核时间")

    class Meta:
        db_table = 'pact_price'
        app_label = 'website'
        verbose_name = verbose_name_plural = "定价协议"
        unique_together = ("pact_type", "company", "partner", "partner_code")

    def __unicode__(self):
        return u"{}({})".format(self.name, self.code)
 

class PactPriceItem(ModelsBase):
    """
        协议定价明细
    """
    parent = models.ForeignKey('PactPrice', null=False, blank=False, db_constraint=False, related_name="items",
                                verbose_name='协议主表', on_delete=models.DO_NOTHING, db_index=True, help_text='协议主表')
    material = models.ForeignKey('MaterialInfo', null=False, blank=False, db_constraint=False,
                               verbose_name='协议物料', on_delete=models.DO_NOTHING, db_index=True, help_text='协议物料')
    material_unit = models.CharField("物料单位", max_length=34, null=True, blank=True, default=None, help_text="该协议的物料单位")
    process_price = models.DecimalField("加工价格", null=False, blank=False, max_digits=16, decimal_places=2, help_text='加工该物料的价格')
    loss_price = models.DecimalField("赔偿价格", null=False, blank=False, max_digits=16, decimal_places=2, help_text='该物料的赔偿价格')

    class Meta:
        db_table = 'pact_price_item'
        app_label = 'website'
        verbose_name = verbose_name_plural = "定价协议明细"
        unique_together = ("parent", "material")

    def __unicode__(self):
        return u"{}({})".format(self.material.name, self.parent.code)