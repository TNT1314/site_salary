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


# 默认单位集合
ENUM_UNIT_ALL = Enum(
    KM='km',
    M='m',
    DM='dm',
    CM='cm',
    MM='mm',
    UM='um',
)
LIST_UNIT_ALL = (
    (ENUM_UNIT_ALL.KM, u'千米'),
    (ENUM_UNIT_ALL.M, u'米'),
    (ENUM_UNIT_ALL.DM, u'分米'),
    (ENUM_UNIT_ALL.CM, u'厘米'),
    (ENUM_UNIT_ALL.MM, u'毫米'),
    (ENUM_UNIT_ALL.UM, u'微米'),
)
DICT_UNIT_ALL = dict(LIST_UNIT_ALL)


# 体积单位集合
ENUM_DIAM_ALL = Enum(
    M='m³',
    DM='dm³',
    CM='cm³',
    MM='mm³',
)
LIST_DIAM_ALL = (
    (ENUM_DIAM_ALL.M, u'立方米'),
    (ENUM_DIAM_ALL.DM, u'立方分米'),
    (ENUM_DIAM_ALL.CM, u'立方厘米'),
    (ENUM_DIAM_ALL.MM, u'立方毫米'),
)
DICT_DIAM_ALL = dict(LIST_DIAM_ALL)


# 重量单位集合
ENUM_WEIGHT_ALL = Enum(
    KG='kg',
    G='g',
    MG='mg',
    UG='ug',
)
LIST_WEIGHT_ALL = (
    (ENUM_WEIGHT_ALL.KG, u'千克'),
    (ENUM_WEIGHT_ALL.G, u'克'),
    (ENUM_WEIGHT_ALL.MG, u'毫克'),
    (ENUM_WEIGHT_ALL.UG, u'微克'),
)
DICT_WEIGHT_ALL = dict(LIST_WEIGHT_ALL)