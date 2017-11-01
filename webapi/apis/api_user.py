#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        site_salary
        用户类业务方法
"""

from mixrestview import ViewSite, fields

from .api_base_view import BaseApiView, CompanyUserApiView
from site_salary.common.backformat import JsonResponse
from webapi.business.bus_user import (
    user_login, user_login_out, get_user_info, get_user_menus,
    get_menus_permission
)


site = ViewSite(name="user", app_name="webapi")


@site
class UserLogin(BaseApiView):
    """
        企业用户登录接口
    """

    def get_context(self, request, *args, **kwargs):

        username = request.params.username
        password = request.params.password

        code, mess, data = user_login(request, username, password)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'login'
        param_fields = (
            ('username', fields.CharField(required=True, help_text=u"企业账号")),
            ('password', fields.CharField(required=True, help_text=u"登录密码")),
        )


@site
class UserLogout(CompanyUserApiView):
    """
        企业用户注销接口
    """

    def get_context(self, request, *args, **kwargs):

        code, mess, data = user_login_out(request)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'logout'


@site
class UserInfoGet(CompanyUserApiView):
    """
        企业用户获取用户信息接口
    """

    def get_context(self, request, *args, **kwargs):

        code, mess, data = get_user_info(request.user)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'info/get'


@site
class UserMenuGet(CompanyUserApiView):
    """
        企业用户获取菜单信息
    """

    def get_context(self, request, *args, **kwargs):

        code, mess, data = get_user_menus(request.user)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'menus/get'


@site
class ModalPermissionGet(CompanyUserApiView):
    """
        企业用户登录接口
    """

    def get_context(self, request, *args, **kwargs):

        modal = request.params.modal

        code, mess, data = get_menus_permission(request.user, modal)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'modal/permission/get'
        param_fields = (
            ('modal', fields.CharField(required=True, help_text=u"模型名称")),
        )

urlpatterns = site.urlpatterns

