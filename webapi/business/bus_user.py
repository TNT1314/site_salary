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
from site_salary.common.imagecode import ImageCodeUtil

from website.models.company_user import CompanyUser
from website.models.user_menu_rel import UserMenuRel
from website.models.group_menu_rel import GroupMenuRel

from webapi.serializers.ser_company_user import S_P_CompanyUser
from webapi.serializers.ser_menus import S_U_Menu


def generate_code_image(wid, hei):
    """
        用户登录方法
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess

    if wid and hei:
        code_image = ImageCodeUtil(size=(wid, hei))
    else:
        code_image = ImageCodeUtil()

    img, v_code = code_image.generate_base64_image4code()

    return code, mess, img, v_code


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


def change_user_info(user, id, avatar, password):
    """
        获取用户信息
        :param user
    """

    data = dict()
    code = ApiCode.success.code
    mess = ApiCode.success.mess

    if user.id == id and avatar or password:
        m_user = CompanyUser.objects.get(pk=user.id)

        fileds = list()
        if avatar:
            m_user.avatar = avatar
            fileds.append("avatar")

        if password:
            m_user.password = password
            fileds.append("password")

        m_user.save(update_fields=fileds)

        data["id"] = m_user.id
    else:
        code = ApiCode.recordserror.code
        mess = ApiCode.recordserror.mess
    return code, mess, data


def search_group_menus(user):
    pass


def search_group_user_menus(user):

    user_menu_relates = UserMenuRel.objects.filter(valid=True, com_user=user, menu__parent__isnull=False)

    user_menus = [relate.menu for relate in user_menu_relates]

    group_menu_relates = GroupMenuRel.objects.filter(valid=True, group=user.group, menu__parent__isnull=False)

    user_group_menus = [relate.menu for relate in group_menu_relates]

    return set(user_menus + user_group_menus)


def search_user_all_menus(user):
    """
        根据用户获取菜单权限
        :param user:
        :return:
    """
    menus = list()

    user_menus = search_group_user_menus(user)

    menu_parents = [menu.parent for menu in user_menus]

    menu_parents = set(menu_parents)

    for parent in menu_parents:

        d_parent = S_U_Menu(parent).data
        d_childs = list()

        for child in user_menus:

            if child.parent.id == parent.id:
                d_childs.append(S_U_Menu(child).data)

        d_parent['childs'] = d_childs

        menus.append(d_parent)

    return menus


def get_user_menus(user):
    """
        获取用户信息
        :param user
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess
    data = dict()
    data['menus'] = list()
    data['menus'] = search_user_all_menus(user)
    return code, mess, data


def get_menus_permission(user, model):
    """
        获取菜单权限
    """

    code = ApiCode.success.code
    mess = ApiCode.success.mess
    data = dict()
    data['permission'] = dict()

    permission = OrderedDict()

    if model in ('help', 'grid'):
        permission['inf'] = True
        permission['add'] = True
        permission['cha'] = True
        permission['aud'] = True
        permission['del'] = True
        permission['pri'] = True
        data['permission'] = permission
    else:
        m_user_menu = UserMenuRel.objects.filter(valid=True, com_user=user, menu__model=model).first()
        m_group_menu = GroupMenuRel.objects.filter(valid=True, group=user.group, menu__model=model).first()

        r_user_menu = UserMenuRel() if not m_user_menu else m_user_menu

        r_group_menu = GroupMenuRel() if not m_group_menu else m_group_menu

        permission['inf'] = getattr(r_user_menu, "p_inf", False) or getattr(r_group_menu, "p_inf", False)
        permission['add'] = getattr(r_user_menu, "p_add", False) or getattr(r_group_menu, "p_add", False)
        permission['cha'] = getattr(r_user_menu, "p_cha", False) or getattr(r_group_menu, "p_cha", False)
        permission['aud'] = getattr(r_user_menu, "p_aud", False) or getattr(r_group_menu, "p_aud", False)
        permission['del'] = getattr(r_user_menu, "p_del", False) or getattr(r_group_menu, "p_del", False)
        permission['pri'] = getattr(r_user_menu, "p_pri", False) or getattr(r_group_menu, "p_pri", False)
        data['permission'] = permission
        data['permission'] = permission

    return code, mess, data