#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-27
    desc: 
        错误对照表
        
        10000为正确， 10000以下为错误， 10000以上为正确
"""


__all__ = ['ApiCode']


from .enum import Enum


ApiCode = Enum(
    unkonwnerror=Enum(code=0, mess="未知错误！"),
    usernotexist=Enum(code=1, mess="用户不存在！"),
    pasworderror=Enum(code=2, mess="用户或密码错误！"),
    unsernologin=Enum(code=3, mess="用户未登录！"),
    nopermission=Enum(code=4, mess="用户未授权！"),
    userhadlogin=Enum(code=5, mess="用户已登录！"),
    edilineerror=Enum(code=6, mess="保存记录出错！"),
    linenoexists=Enum(code=7, mess="请求的记录不存在！"),
    submitsecond=Enum(code=8, mess="重复提交！"),
    logincodeerr=Enum(code=10, mess="验证码实效，请重新获取！"),
    recordserror=Enum(code=11, mess="没有数据权限！"),
    repeatserror=Enum(code=12, mess="数据重复！"),

    success=Enum(code=10000, mess="请求成功。"),
)