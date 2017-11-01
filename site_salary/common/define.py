#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        site_salary
"""

from .enum import Enum


# 上传文件存储未知
ENUM_IMAGE_PATH = Enum(
    COMPANYUSER="company/user/",
)

LIST_IMAGE_PATH = (
    (ENUM_IMAGE_PATH.COMPANYUSER, u'用户头像'),
)

DICT_IMAGE_PATH = dict(LIST_IMAGE_PATH)

# 性别
ENUM_EMPLOYEE_GENDER = Enum(
    MALE=1,
    FEMALE=2,
)
LIST_EMPLOYEE_GENDER = (
    (ENUM_EMPLOYEE_GENDER.MALE, u'男'),
    (ENUM_EMPLOYEE_GENDER.FEMALE, u'女'),
)
DICT_EMPLOYEE_GENDER = dict(LIST_EMPLOYEE_GENDER)

# 员工状态
ENUM_EMPLOYEE_STATUS = Enum(
    OFLINE=0,
    ONLINE=1,
    STLINE=2,
)
LIST_EMPLOYEE_STATUS = (
    (ENUM_EMPLOYEE_STATUS.OFLINE, u'离职'),
    (ENUM_EMPLOYEE_STATUS.ONLINE, u'在职'),
    (ENUM_EMPLOYEE_STATUS.STLINE, u'停薪留职'),
)
DICT_EMPLOYEE_STATUS = dict(LIST_EMPLOYEE_STATUS)