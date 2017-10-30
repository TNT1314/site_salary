#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        抽象类
"""


import time
from django.db import models
from django.utils.encoding import force_text
from django.db import transaction, OperationalError
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField
)


class TimeFieldModel(models.Model):
    create_time = CreationDateTimeField('创建时间', db_index=True, editable=False)
    change_time = ModificationDateTimeField('修改时间', db_index=True, editable=False)

    class Meta:
        abstract = True
        get_latest_by = 'change_time'
        ordering = ('-change_time', '-create_time',)

    def __unicode__(self):
        return unicode("{}({})".format(self.__class__.__name__, self.pk))

    def history_log(self, user, action=CHANGE, message=''):
        """
            Log that an object has been successfully changed.
            The default implementation creates an admin LogEntry object.
        """
        LogEntry.objects.log_action(
            user_id=user.pk,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=self.pk,
            object_repr=force_text(self),
            action_flag=action,
            change_message=message
        )


class ModelsBase(TimeFieldModel):
    """
        model 抽象类
    """
    valid = models.BooleanField("有效", default=True, null=False, db_index=True)
    remarks = models.CharField('备注', max_length=500, null=True, blank=True)

    create_user = models.ForeignKey("auth.user", default=None,
            editable=False, null=True, blank=True, on_delete=models.DO_NOTHING,
            related_name='+', db_constraint=False, verbose_name='创建人员', db_index=True)
    change_user = models.ForeignKey("auth.user", default=None,
            editable=False, null=True, blank=True, on_delete=models.DO_NOTHING,
            related_name='+', db_constraint=False, verbose_name='修改人员', db_index=True)

    @staticmethod
    def autocomplete_search_fields():
        return ['pk__exact']

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if update_fields:

            fd = [f.name for f in self._meta.fields]

            for f in update_fields:

                if f not in fd: update_fields.remove(f)

            # change the change_time
            if 'change_time' not in update_fields:

                update_fields.append('change_time')

        self.change_logging(force_insert=force_insert, force_update=force_update,
                            using=using, update_fields=update_fields)

    def change_logging(self, force_insert=None, force_update=None, using=None, update_fields=None):
        try:
            TimeFieldModel.save( self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        except OperationalError as exp:
            if exp.args[0] == 1213 and not transaction.is_dirty(self._state.db):
                time.sleep(0.01)
                return TimeFieldModel.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
                )
            raise