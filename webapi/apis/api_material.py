#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-06
    desc: 
        site_salary
        物料信息api接口
"""

from mixrestview import ViewSite, fields

from .api_base_view import CompanyUserApiView
from site_salary.common.backformat import JsonResponse
from webapi.business.bus_material import (
    user_get_materials_pager, user_get_material
)

site = ViewSite(name="material", app_name="webapi")


@site
class MaterialList(CompanyUserApiView):
    """
        物料列表
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        code = request.params.code
        name = request.params.name
        help = request.params.help

        pagesize = request.params.pagesize
        pagenum = request.params.pagenum
        sortdatafield = request.params.sortdatafield
        sortorder = request.params.sortorder

        code, mess, data = user_get_materials_pager(
            user, pagesize, pagenum, sortdatafield, sortorder,
            code, name, help
        )
        return JsonResponse(code, mess, data)

    class Meta:
        path = 'list/get'
        param_fields = (
            ('pagesize', fields.IntegerField(required=True, help_text=u"页面数据")),
            ('pagenum', fields.IntegerField(required=True, help_text=u"当前页数")),
            ('sortdatafield', fields.CharField(required=False, help_text=u"排序字段")),
            ('sortorder', fields.CharField(required=False, help_text=u"排序方式（asc:升序,des:降序）")),

            ('code', fields.CharField(required=False, help_text=u"物料编码")),
            ('name', fields.CharField(required=False, help_text=u"物料名称")),
            ('help', fields.CharField(required=False, help_text=u"物料助记码")),
        )


@site
class MaterialGet(CompanyUserApiView):
    """
        根据物料ID获取物料信息
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        id = request.params.id

        code, mess, data = user_get_material(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'get'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"唯一ID")),
        )


urlpatterns = site.urlpatterns