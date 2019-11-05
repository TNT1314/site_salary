#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-15
    desc: 
        site_salary
"""

from mixrestview import ViewSite, fields

from .api_base_view import CompanyUserApiView
from site_salary.common.regular import valid_mobile
from site_salary.common.backformat import JsonResponse
from site_salary.common.define import LIST_PACK_STATUS

from webapi.business.bus_pact_price import (
    get_pact_price_pager, get_pact_price_by_id, 
    cha_pact_price, add_pact_price,
    audit_pact_price, delete_pact_price,
)


site = ViewSite(name="pact_price", app_name="webapi")


@site
class PactPriceList(CompanyUserApiView):
    """
        获取定价协议分页列表
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        partner = request.params.partner
        partner_code = request.params.partner_code

        pagesize = request.params.pagesize
        pagenum = request.params.pagenum
        sort_field = request.params.sortdatafield
        sort_order = request.params.sortorder

        code, mess, data = get_pact_price_pager(user, pagesize, pagenum, partner, partner_code, sort_field, sort_order)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'list/get'
        param_fields = (
            ('pagesize', fields.IntegerField(required=True, help_text=u"页面数据")),
            ('pagenum', fields.IntegerField(required=True, help_text=u"当前页数")),
            ('partner', fields.IntegerField(required=False, help_text=u"伙伴拼音码")),
            ('partner_code', fields.CharField(required=False, help_text=u"伙伴名称")),
            ('sortdatafield', fields.CharField(required=False, help_text=u"排序字段")),
            ('sortorder', fields.CharField(required=False, help_text=u"排序方式（asc:升序,des:降序）")),
        )


@site
class PactPriceGet(CompanyUserApiView):
    """
        获取定价协议明细
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        id = request.params.id

        code, mess, data = get_pact_price_by_id(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'get'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"记录ID")),
        )


@site
class PactPriceChange(CompanyUserApiView):
    """
        修改定价协议
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        id = request.params.id
        pact_type = request.params.pact_type
        partner = request.params.partner
        partner_code = request.params.partner_code
        send_man = request.params.send_man
        send_man_phone = request.params.send_man_phone
        send_address = request.params.send_address
        remarks = request.params.remarks
        items = request.params.items

        if id:
            code, mess, data = cha_pact_price(user, id, pact_type, partner, partner_code,
        send_man, send_man_phone, send_address, remarks, items)
        else:
            code, mess, data = add_pact_price(user, pact_type, partner, partner_code,
        send_man, send_man_phone, send_address, remarks, items)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'change'
        param_fields = (
            ('id', fields.IntegerField(required=False, help_text=u"记录ID")),
            ('pact_type', fields.ChoiceField(required=True, choices=LIST_PACK_STATUS, help_text=u"协议类型")),
            ('partner', fields.IntegerField(required=True, help_text=u"伙伴ID")),
            ('partner_code', fields.CharField(required=True, help_text=u"伙伴合同编号")),
            ('send_man', fields.CharField(required=True, help_text=u"收货人")),
            ('send_man_phone', fields.RegexField(valid_mobile,required=True, help_text=u"收货人电话")),
            ('send_address', fields.CharField(required=True, help_text=u"送货地址")),
            ('remarks', fields.CharField(required=True, help_text=u"记录ID")),
            ('items', fields.CharField(required=True, help_text=u"明细字段")),
        )


@site
class PactPriceAudit(CompanyUserApiView):
    """
        审核定价协议
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        id = request.params.id

        code, mess, data = audit_pact_price(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'audit'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"记录ID")),
        )


@site
class PactPriceDelete(CompanyUserApiView):
    """
        删除定价协议
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        id = request.params.id

        code, mess, data = delete_pact_price(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'delete'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"记录ID")),
        )


urlpatterns = site.urlpatterns
 
