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

from collections import OrderedDict


def JsonResponse(code, mess, data):
    back_data = OrderedDict()
    back_data["code"] = code
    back_data["code_desc"] = mess
    back_data["json"] = dict()
    back_data["json"] = data
    return back_data


def JsonpResponse(code, mess, **kwargs):
    back_data = OrderedDict()
    back_data["code"] = code
    back_data["code_desc"] = mess
    back_data.update(**kwargs)
    return back_data


def MessResponse(code, mess, **kwargs):
    back_data = OrderedDict()
    back_data["code"] = code
    back_data["code_desc"] = mess
    back_data.update(kwargs)
    return back_data