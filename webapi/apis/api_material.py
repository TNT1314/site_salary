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
from site_salary.common.define import (
    LIST_UNIT_ALL,LIST_BULK_ALL,LIST_WEIGHT_ALL
)
from webapi.business.bus_material import (
    user_get_materials_pager, user_get_material,
    user_add_material, user_update_material
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

@site
class MaterialChange(CompanyUserApiView):
    """
        添加企业员工
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        name = request.params.name
        length = request.params.length
        length_unit = request.params.length_unit
        wide = request.params.wide
        wide_unit = request.params.wide_unit
        height = request.params.height
        height_unit = request.params.height_unit
        diam = request.params.diam
        diam_unit = request.params.diam_unit
        bulk = request.params.bulk
        bulk_unit = request.params.bulk_unit
        weight = request.params.weight
        weight_unit = request.params.weight_unit


        id = request.params.id

        if id:
            code, mess, data = user_update_material(
                user, id, name, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit
            )
        else:
            code, mess, data = user_add_material(
                user, name, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit
            )

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'change'
        param_fields = (
            ('id', fields.CharField(required=False, help_text=u"修改某个员工的唯一标识")),
            ('name', fields.CharField(required=True, help_text=u"新增员工的姓名")),
            ('length', fields.IntegerField(required=False, help_text=u"物料长度")),
            ('length_unit', fields.ChoiceField(required=True, choices=LIST_UNIT_ALL, help_text=u"长度单位")),
            ('wide', fields.IntegerField(required=False, help_text=u"物料宽度")),
            ('wide_unit', fields.ChoiceField(required=True, choices=LIST_UNIT_ALL, help_text=u"宽度单位")),
            ('height', fields.IntegerField(required=False, help_text=u"物料高度")),
            ('height_unit', fields.ChoiceField(required=True, choices=LIST_UNIT_ALL, help_text=u"高度单位")),
            ('diam', fields.IntegerField(required=False, help_text=u"物料直径")),
            ('diam_unit', fields.ChoiceField(required=True, choices=LIST_UNIT_ALL, help_text=u"直径单位")),
            ('bulk', fields.IntegerField(required=False, help_text=u"物料体积")),
            ('bulk_unit', fields.ChoiceField(required=True, choices=LIST_BULK_ALL, help_text=u"体积单位")),
            ('weight', fields.IntegerField(required=False, help_text=u"物料重量")),
            ('weight_unit', fields.ChoiceField(required=True, choices=LIST_WEIGHT_ALL, help_text=u"重量单位")),
        )

urlpatterns = site.urlpatterns