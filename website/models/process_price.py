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

__all__ = ['ProcessPrice']


from django.db import models
from .base_model import ModelsBase


class ProcessPrice(ModelsBase):
    """
        物料加工定价
    """

    material = models.OneToOneField('MaterialInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='物料信息', on_delete=models.DO_NOTHING, db_index=True, help_text='物料信息')
    price = models.DecimalField("加工价格", null=False, blank=False, max_digits=16, decimal_places=4, help_text='加工该物料的价格')
    unit = models.CharField("计件单位", max_length=100, null=False, blank=False, default="件", help_text='计件单位')

    class Meta:
        db_table = 'process_price'
        app_label = 'website'
        verbose_name = verbose_name_plural = '物料加工定价'

    def __unicode__(self):
        return u"{}:{}({})".format(self.material.name, self.price, self.material.standards)
