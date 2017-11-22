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

from django.contrib.auth.models import AnonymousUser

from .api_base_view import BaseApiView, CompanyUserApiView

from site_salary.common.apicode import ApiCode
from site_salary.common.backformat import JsonResponse
from webapi.business.bus_user import (
    generate_code_image, user_login, user_login_out, get_user_info,
    get_user_menus, get_menus_permission, change_user_info
)


site = ViewSite(name="user", app_name="webapi")

@site
class GeneratorImageCode(BaseApiView):
    """
        生成随机验证码
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        if isinstance(user, AnonymousUser) :
            request.session.save()
            wid = request.params.wid
            hei = request.params.hei

            code, mess, data, vcode = generate_code_image(wid, hei)

            request.session['vcode'] = vcode
        else:
            code = ApiCode.userhadlogin.code
            mess = ApiCode.userhadlogin.mess
            data = dict()
        return JsonResponse(code, mess, data)

    class Meta:
        path = 'login/vcode/get'
        param_fields = (
            ('wid', fields.IntegerField(required=False, help_text=u"生成验证码的宽度")),
            ('hei', fields.IntegerField(required=False, help_text=u"生成验证码的长度")),
        )


@site
class UserLogin(BaseApiView):
    """
        企业用户登录接口
    """

    def get_context(self, request, *args, **kwargs):

        vcode = request.params.vcode

        username = request.params.username
        password = request.params.password

        back_vcode = request.session['vcode'] if request.session.has_key('vcode') else None

        if back_vcode and vcode.upper() == back_vcode:
            code, mess, data = user_login(request, username, password)
            del request.session['vcode']

        elif not back_vcode:
            data = dict()
            code = ApiCode.logincodeerr.code
            mess = ApiCode.logincodeerr.mess

        else:
            data = dict()
            code = ApiCode.unkonwnerror.code
            mess = ApiCode.unkonwnerror.mess
        return JsonResponse(code, mess, data)

    class Meta:
        path = 'login'
        param_fields = (
            ('username', fields.CharField(required=True, help_text=u"企业账号")),
            ('password', fields.CharField(required=True, help_text=u"登录密码")),
            ('vcode', fields.CharField(required=True, help_text=u"验证码")),
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
class UserInfoChange(CompanyUserApiView):
    """
        企业用户修改用户信息接口
    """

    def get_context(self, request, *args, **kwargs):

        id = request.params.id
        avatar = request.params.avatar
        password = request.params.password

        code, mess, data = change_user_info(request.user, id, avatar, password)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'info/change'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"用户唯一表示")),
            ('avatar', fields.CharField(required=False, help_text=u"头像")),
            ('password', fields.CharField(required=False, help_text="密码")),

        )

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
class ModelPermissionGet(CompanyUserApiView):
    """
        企业用户登录接口
    """

    def get_context(self, request, *args, **kwargs):

        model = request.params.model

        code, mess, data = get_menus_permission(request.user, model)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'model/permission/get'
        param_fields = (
            ('model', fields.CharField(required=True, help_text=u"模型名称")),
        )

urlpatterns = site.urlpatterns

