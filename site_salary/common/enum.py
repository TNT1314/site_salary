#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        枚举类型
"""


class Enum(object):
    """
        枚举类型，处理枚举数据
    """
    def __init__(self, **kwargs):
        for attr, val in kwargs.iteritems():
            setattr(self, attr, val)