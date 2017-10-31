#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-27
    desc: 
        企业用户业务类
"""

from collections import OrderedDict
from django.contrib.auth import (
    authenticate, login, logout
)

from site_salary.common.apicode import ApiCode

from website.models.menu_info import MenuInfo
from website.models.company_user import CompanyUser
from website.models.user_menu_rel import UserMenuRel

from webapi.serializers.ser_company_user import S_P_CompanyUser
from webapi.serializers.ser_menus import S_U_Menus


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
    mess = ApiCode.success.mess
    data = dict()

    if isinstance(request.user, CompanyUser):

        code = ApiCode.userhadlogin.code
        mess = ApiCode.userhadlogin.mess

    else:

        m_user = authenticate(username=username, password=password)

        if not m_user:

            code = ApiCode.pasworderror.code
            mess = ApiCode.pasworderror.mess

        else:
            if m_user.valid:

                login(request, m_user)

            else:

                code = ApiCode.pasworderror.code
                mess = ApiCode.pasworderror.mess

    return code, mess, data


def user_login_out(request):
    """
        用户登出系统
        :param request:
        :return:
    """
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    logout(request)

    return code, mess, dict()



def get_user_info(user):
    """
        获取用户信息
        :param user
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess

    m_user = CompanyUser.objects.get(pk=user.id)
    s_user = S_P_CompanyUser(m_user)

    data = s_user.data
    return code, mess, data


def search_user_menus(user):
    """
        根据用户获取菜单权限
        :param user:
        :return:
    """
    menus = list()

    m_user_menu_rels = UserMenuRel.objects.filter(com_user=user, menu__parent__isnull=False)

    menu_childs = [relate.menu for relate in m_user_menu_rels]

    menu_parents = (relate.menu.parent for relate in m_user_menu_rels)

    for parent in menu_parents:

        d_parent = S_U_Menus(parent).data
        d_childs = list()

        for child in menu_childs:

            if child.parent.id == parent.id:
                d_childs.append(S_U_Menus(child).data)

        d_parent['childs'] = d_childs

        menus.append(d_parent)

    return menus



def get_user_info(user):
    """
        获取用户信息
        :param user
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess
    data = dict()
    data['menus'] = list()
    data['menus'] = search_user_menus(user)
    return code, mess, data
