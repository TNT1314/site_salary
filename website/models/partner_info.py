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

__all__ = ['PartnerInfo']

from django.db import models
from .base_model_com import ModelsBase


class PartnerInfo(ModelsBase):
    """
        合作伙伴
    """

    code = models.CharField('伙伴编码', max_length=50, null=True, blank=True, help_text="该合作伙伴中文简拼")
    name = models.CharField('伙伴名称', max_length=500, null=False, blank=False, help_text="该合作伙伴的中文名称")
    short_name = models.CharField('伙伴简称', max_length=500, null=False, blank=False, help_text="该合作伙伴的中文简拼")
    supplier = models.BooleanField('供应商', null=False, blank=False, default=False, help_text="该合作伙伴是否为供应商")
    customer = models.BooleanField('客户', null=False, blank=False, default=False, help_text="该合作伙伴是否为客户")

    phone = models.CharField("伙伴联系方式", max_length=14, null=True, blank=True, default=None, help_text="该合作伙伴的电话号码")
    society_code = models.CharField("统一社会信用代码证", max_length=34, null=True, blank=True, default=None, help_text="该合作伙伴的统一社会信用证")
    link_man = models.CharField("伙伴联系人", max_length=100, null=True, blank=True, default=None, help_text="该合作伙伴的联系人员")
    link_man_phone = models.CharField("伙伴联系人电话", max_length=34, null=True, blank=True, default=None, help_text="该合作伙伴的联系人员电话")

    send_man = models.CharField("伙伴收货人", max_length=34, null=True, blank=True, default=None, help_text="该合作伙伴的收货人电话")
    send_man_phone = models.CharField("伙伴收货人电话", max_length=34, null=True, blank=True, default=None, help_text="该合作伙伴的收货人电话")
    address = models.CharField('伙伴地址', max_length=500, null=True, blank=True, help_text="改合作伙伴的办公地址，会默认为收货地址")

    company = models.ForeignKey('CompanyInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='公司信息', on_delete=models.DO_NOTHING, db_index=True, help_text='对应公司')

    class Meta:
        db_table = 'partner_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = "合作伙伴"

    def __unicode__(self):
        return u"{}({})".format(self.name, self.code)
 
