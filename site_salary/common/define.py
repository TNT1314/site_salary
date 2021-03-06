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
ENUM_BULK_ALL = Enum(
    M='m³',
    DM='dm³',
    CM='cm³',
    MM='mm³',
)
LIST_BULK_ALL = (
    (ENUM_BULK_ALL.M, u'立方米'),
    (ENUM_BULK_ALL.DM, u'立方分米'),
    (ENUM_BULK_ALL.CM, u'立方厘米'),
    (ENUM_BULK_ALL.MM, u'立方毫米'),
)
DICT_BULK_ALL = dict(LIST_BULK_ALL)


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


# 季度选项
ENUM_QUARTER_ALL = Enum(
    ONE=1,
    TWO=2,
    THR=3,
    FOU=4,
    FIV=5,
    SIX=6,
    SEV=7,
    EGT=8,
    NIN=9,
    TEN=10,
    ELE=11,
    TWE=12
)
LIST_QUARTER_ALL = (
    (ENUM_QUARTER_ALL.ONE, u'一月'),
    (ENUM_QUARTER_ALL.TWO, u'二月'),
    (ENUM_QUARTER_ALL.THR, u'三月'),
    (ENUM_QUARTER_ALL.FOU, u'四月'),
    (ENUM_QUARTER_ALL.FIV, u'五月'),
    (ENUM_QUARTER_ALL.SIX, u'六月'),
    (ENUM_QUARTER_ALL.SEV, u'七月'),
    (ENUM_QUARTER_ALL.EGT, u'八月'),
    (ENUM_QUARTER_ALL.NIN, u'九月'),
    (ENUM_QUARTER_ALL.TEN, u'十月'),
    (ENUM_QUARTER_ALL.ELE, u'十一月'),
    (ENUM_QUARTER_ALL.TWE, u'十二月'),
)
DICT_QUARTER_ALL = dict(LIST_QUARTER_ALL)


# 单据状态选项
ENUM_STATUS_ALL = Enum(
    NEW=1,
    AUD=2,
)
LIST_STATUS_ALL = (
    (ENUM_STATUS_ALL.NEW, u'新增'),
    (ENUM_STATUS_ALL.AUD, u'已审核'),

)
DICT_STATUS_ALL = dict(LIST_STATUS_ALL)


# 协议类型
ENUM_PACT_TYPE = Enum(
    JG='JG',
    CG='CG',
    XS='XS',
)
LIST_PACT_TYPE = (
    (ENUM_PACT_TYPE.JG, u'加工'),
    (ENUM_PACT_TYPE.CG, u'采购'),
    (ENUM_PACT_TYPE.XS, u'销售'),
)
DICT_PACT_TYPE = dict(LIST_PACT_TYPE)


# 状态
ENUM_PACK_STATUS = Enum(
    XZ='XZ',
    SH='SH',
    JY='JY',
)
LIST_PACK_STATUS = (
    (ENUM_PACK_STATUS.XZ, u'新增'),
    (ENUM_PACK_STATUS.SH, u'审核'),
    (ENUM_PACK_STATUS.JY, u'禁用'),
)
DICT_PACK_STATUS = dict(LIST_PACK_STATUS)