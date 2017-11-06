#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals


""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-06
    desc: 
        基础物料信息表
"""

__all__ = ['MaterialInfo']

from django.db import models
from .base_model import ModelsBase
from site_salary.common.untils import chinese2pinyin
from site_salary.common.define import (
    ENUM_UNIT_ALL, LIST_UNIT_ALL,
    ENUM_BULK_ALL, LIST_BULK_ALL,
    ENUM_WEIGHT_ALL, LIST_WEIGHT_ALL,
)


class MaterialInfo(ModelsBase):
    """
        物料信息基础表
    """

    code = models.CharField('物料编码', max_length=30, null=True, blank=True, help_text="物料编码（物料拼音码）")
    name = models.CharField('物料名称', max_length=100, null=True, blank=True, help_text="物料名称")
    help = models.CharField('助记字段', max_length=10, null=True, blank=True, help_text="物料辅助记录")
    standards = models.CharField('物料规格', max_length=100, null=True, blank=True, help_text="物料规格，从长宽高等汇总")
    length = models.IntegerField('物料长度', null=True, blank=True, help_text="单一物料的长度")
    length_unit = models.CharField('长度单位', max_length=10, null=True, blank=True, choices=LIST_UNIT_ALL, default=ENUM_UNIT_ALL.M,
                                   help_text="物料的长度单位")
    wide = models.IntegerField('物料宽度', null=True, blank=True, help_text="单一物料宽度")
    wide_unit = models.CharField('宽度单位', max_length=10, null=True, blank=True, choices=LIST_UNIT_ALL, default=ENUM_UNIT_ALL.M,
                                 help_text="物料的高度单位")
    height = models.IntegerField('物料高度', null=True, blank=True, help_text="单一物料的高度")
    height_unit = models.CharField('高度单位', max_length=10, null=True, blank=True, choices=LIST_UNIT_ALL, default=ENUM_UNIT_ALL.M,
                                   help_text="物料的高度单位")
    diam = models.IntegerField('物料直径', null=True, blank=True, help_text="单一物料的直径")
    diam_unit = models.CharField('直径单位', max_length=10, null=True, blank=True, choices=LIST_UNIT_ALL, default=ENUM_UNIT_ALL.M,
                                 help_text="物料的高度单位")
    bulk = models.IntegerField('物料体积', null=True, blank=True, help_text="单一物料体积")
    bulk_unit = models.CharField('体积单位', max_length=10, null=True, blank=True, choices=LIST_BULK_ALL, default=ENUM_BULK_ALL.M,
                                 help_text="物料的高度单位")
    weight = models.IntegerField('物料重量', null=True, blank=True, help_text="单一物料重量")
    weight_unit = models.CharField('重量单位', max_length=10, null=True, blank=True, choices=LIST_WEIGHT_ALL, default=ENUM_WEIGHT_ALL.KG,
                                   help_text="物料的高度单位")
    company = models.ForeignKey('CompanyInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='公司信息', on_delete=models.DO_NOTHING, db_index=True, help_text='所属公司')

    class Meta:
        db_table = 'material_info'
        app_label = 'website'
        verbose_name = verbose_name_plural = '物料信息'
        unique_together = ['company', 'code', 'standards']

    def __unicode__(self):
        return u"{}({})".format(self.name, self.standards)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
            重写save方法
            :param force_insert:
            :param force_update:
            :param using:
            :param update_fields:
            :return:
        """

        stand_list = list()

        if self.length:
            stand_list.append("L{}{}".format(self.length, self.length_unit))

        if self.wide:
            stand_list.append("W{}{}".format(self.wide, self.wide_unit))

        if self.height:
            stand_list.append("H{}{}".format(self.height, self.height_unit))

        if self.diam:
            stand_list.append("Φ{}{}".format(self.diam, self.diam_unit))

        if self.bulk:
            stand_list.append("V{}{}".format(self.bulk, self.bulk_unit))

        if self.weight:
            stand_list.append("M{}{}".format(self.weight, self.weight_unit))

        self.standards = "*".join(stand_list)

        self.code = chinese2pinyin(self.name).upper()

        super(MaterialInfo, self).save(force_insert=False, force_update=False, using=None, update_fields=None)