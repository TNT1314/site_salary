#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-07
    desc: 
        site_salary
"""

from mixrestview import ViewSite, fields

from .api_base_view import CompanyUserApiView
from site_salary.common.backformat import JsonResponse
from site_salary.common.define import (
    LIST_UNIT_ALL, LIST_BULK_ALL, LIST_WEIGHT_ALL
)
from webapi.business.bus_process_price import (
    user_get_process_price_pager, user_get_process_price,
    user_add_process_price, user_update_process_price,
    user_get_process_price_simple
)


site = ViewSite(name="process_price", app_name="webapi")


@site
class ProcessPriceList(CompanyUserApiView):
    """
        物料定价列表
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

        code, mess, data = user_get_process_price_pager(
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
class ProcessPriceGet(CompanyUserApiView):
    """
        获取物料定价详细信息接口
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        id = request.params.id

        code, mess, data = user_get_process_price(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'get'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"物料定价唯一ID")),
        )


@site
class ProcessPriceChange(CompanyUserApiView):
    """
        修改物料加工定价接口
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
        price = request.params.price
        unit = request.params.unit

        id = request.params.id

        if id:
            code, mess, data = user_update_process_price(
                user, id, name, price, unit, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit
            )
        else:
            code, mess, data = user_add_process_price(
                user, name, price, unit, length, length_unit, wide, wide_unit,
                height, height_unit, diam, diam_unit, bulk, bulk_unit,
                weight, weight_unit
            )

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'change'
        param_fields = (
            ('id', fields.CharField(required=False, help_text=u"修改某个员工的唯一标识")),
            ('name', fields.CharField(required=True, help_text=u"新增员工的姓名")),
            ('price', fields.DecimalField(required=True, max_digits=16, decimal_places=4, help_text="物料加工价格")),
            ('unit', fields.CharField(required=True, help_text="物料计件单位")),
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

@site
class ProcessPriceGetByID(CompanyUserApiView):
    """
        获取物料定价详细信息接口
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        name = request.params.name

        code, mess, data = user_get_process_price_simple(user, name)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'select/get'
        param_fields = (
            ('name', fields.CharField(required=False, help_text=u"物料定价唯一ID")),
        )

urlpatterns = site.urlpatterns
