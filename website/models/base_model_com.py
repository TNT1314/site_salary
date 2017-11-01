#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/11/1 23:27
    @description:
        公司用户类
"""

import time
from django.db import models
from django.db import transaction, OperationalError
from .base_model import CompanyTimeFieldModel


class ModelsBase(CompanyTimeFieldModel):
    """
        company model 抽象类
    """

    valid = models.BooleanField("有效", default=True, null=False, db_index=True)
    remarks = models.CharField('备注', max_length=500, null=True, blank=True)

    add_com_user = models.ForeignKey("CompanyInfo", default=None,
            editable=False, null=True, blank=True, on_delete=models.DO_NOTHING,
            related_name='+', db_constraint=False, verbose_name='创建人员', db_index=True)
    cha_com_user = models.ForeignKey("CompanyInfo", default=None,
            editable=False, null=True, blank=True, on_delete=models.DO_NOTHING,
            related_name='+', db_constraint=False, verbose_name='修改人员', db_index=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if update_fields:

            fd = [f.name for f in self._meta.fields]

            for f in update_fields:

                if f not in fd: update_fields.remove(f)

            # change the change_time
            if 'cha_com_time' not in update_fields:

                update_fields.append('cha_com_time')

        self.change_logging(force_insert=force_insert, force_update=force_update,
                            using=using, update_fields=update_fields)

    def change_logging(self, force_insert=None, force_update=None, using=None, update_fields=None):
        try:
            CompanyTimeFieldModel.save( self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        except OperationalError as exp:
            if exp.args[0] == 1213 and not transaction.is_dirty(self._state.db):
                time.sleep(0.01)
                return CompanyTimeFieldModel.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
            raise