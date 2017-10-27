#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-27
    desc: 
        企业用户业务类
"""

from django.contrib.auth import (
    authenticate, login, logout
)

from site_salary.common.apicode import ApiCode
from website.models.company_user import CompanyUser
from webapi.serializers.ser_company_user import S_P_CompanyUser

def user_login(request, username, password):
    """
        用户登录方法
        :param request:
        :param username:
        :param password:
        :param user:
        :return:
    """

    code = ApiCode.success.code
    mesg = ApiCode.success.mesg
    data = dict()

    if isinstance(request.user, CompanyUser):

        code = ApiCode.userhadlogin.code
        mesg = ApiCode.userhadlogin.mesg

    else:

        m_user = authenticate(username=username, password=password)

        if not m_user:

            code = ApiCode.pasworderror.code
            mesg = ApiCode.pasworderror.mesg
        else:
            if m_user.valid:
                login(request, m_user)
            else:
                code = ApiCode.pasworderror.code
                mesg = ApiCode.pasworderror.mesg
    return code, mesg, data


def get_user_info(user):
    """
        获取用户信息
        :param user
    """
    
    code = ApiCode.success.code
    mesg = ApiCode.success.mesg

    m_user = CompanyUser.objects.get(pk=user.id)
    s_user = S_P_CompanyUser(m_user)

    data = s_user.data
    return code, mesg, data
