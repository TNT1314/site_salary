#! usr/bin/env python
# encoding: utf-8
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