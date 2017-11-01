#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        前端用户模型
"""

__all__ = ['CompanyUser']


from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .base_model import ModelsBase
from site_salary.common.untils import upload_path, password2md5

class CompanyUser(AbstractBaseUser, ModelsBase):
    """
        公司用户模型
    """

    is_staff = False
    USERNAME_FIELD = 'username'

    username = models.CharField('用户名', max_length=200, unique=True, null=False, blank=False, help_text='用户名，用于登录')
    name = models.CharField('真实姓名', max_length=100, unique=True, null=False, blank=False, help_text='真实姓名')
    mobile = models.BigIntegerField('电话号码', null=False, blank=False, unique=True, db_index=True, help_text='手机号码')
    email = models.EmailField('电子邮箱', null=True, blank=True, default=None, help_text='用于找回密码')
    avatar = models.ImageField('头像', default=None, upload_to=upload_path, null=True, blank=True, help_text='个性头像')
    company = models.ForeignKey('CompanyInfo', null=False, blank=False, db_constraint=False,
                                verbose_name='公司信息', on_delete=models.DO_NOTHING, db_index=True, help_text='对应公司')
    group = models.ForeignKey('GroupInfo', null=True, blank=True, db_constraint=False,
                                verbose_name='分组信息', on_delete=models.DO_NOTHING, db_index=True, help_text='分组信息')

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def set_password(self, raw_password):
        self.password = password2md5(self.password, self.username)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(CompanyUser, self).save(*args, **kwargs)

    class Meta:
        db_table = 'company_user'
        app_label = 'website'
        verbose_name = verbose_name_plural = '公司账号信息'

    def __unicode__(self):
        return u'{}({})'.format(self.username, self.mobile)