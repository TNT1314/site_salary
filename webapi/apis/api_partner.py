#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-12-13
    desc: 
        site_salary
"""


from mixrestview import ViewSite, fields

from .api_base_view import CompanyUserApiView
from site_salary.common.backformat import JsonResponse
from site_salary.common.regular import valid_tell, valid_social, valid_mobile
from webapi.business.bus_partner import (
    user_get_partners_pager, user_add_partner, user_change_partner,
    user_get_partner_by_id, get_partner_by_term
)


site = ViewSite(name="partner", app_name="webapi")


@site
class PartnerList(CompanyUserApiView):
    """
        合作伙伴公司
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        code = request.params.code
        name = request.params.name
        pagesize = request.params.pagesize
        pagenum = request.params.pagenum
        sort_field = request.params.sortdatafield
        sort_order = request.params.sortorder

        code, mess, data = user_get_partners_pager(user, pagesize, pagenum, code, name, sort_field, sort_order)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'list/get'
        param_fields = (
            ('pagesize', fields.IntegerField(required=True, help_text=u"页面数据")),
            ('pagenum', fields.IntegerField(required=True, help_text=u"当前页数")),
            ('code', fields.CharField(required=False, help_text=u"伙伴拼音码")),
            ('name', fields.CharField(required=False, help_text=u"伙伴名称")),
            ('sortdatafield', fields.CharField(required=False, help_text=u"排序字段")),
            ('sortorder', fields.CharField(required=False, help_text=u"排序方式（asc:升序,des:降序）")),
        )


@site
class PartnerChange(CompanyUserApiView):
    """
        合作伙伴公司
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        id = request.params.id
        name = request.params.name
        short_name = request.params.short_name
        supplier = request.params.supplier
        customer = request.params.customer
        phone = request.params.phone
        society_code = request.params.society_code
        link_man = request.params.link_man
        link_man_phone = request.params.link_man_phone
        send_man = request.params.send_man
        send_man_phone = request.params.send_man_phone
        address = request.params.address

        if not id:
            code, mess, data = user_add_partner(
                user, name, short_name, supplier, customer, phone, society_code,
                link_man, link_man_phone, send_man, send_man_phone, address)
        else:
            code, mess, data = user_change_partner(
                user, id, name, short_name, supplier, customer, phone, society_code,
                link_man, link_man_phone, send_man, send_man_phone, address)
        return JsonResponse(code, mess, data)

    class Meta:
        path = 'change'
        param_fields = (
            ('id', fields.IntegerField(required=False, help_text=u"数据唯一ID")),
            ('name', fields.CharField(required=True, help_text=u"伙伴名称")),
            ('short_name', fields.CharField(required=False, help_text=u"伙伴名称")),
            ('supplier', fields.BooleanField(required=False, help_text=u"是否供应商")),
            ('customer', fields.BooleanField(required=False, help_text=u"是否客户")),
            ('phone', fields.RegexField(valid_tell, required=False, help_text=u"用户座机号码")),
            ('society_code', fields.RegexField(valid_social, required=False, help_text=u"用户座机号码")),
            ('link_man', fields.CharField(required=False, help_text=u"联系人")),
            ('link_man_phone', fields.RegexField(valid_mobile, required=False, help_text=u"联系人电话号码")),
            ('send_man', fields.CharField(required=False, help_text=u"收货人")),
            ('send_man_phone', fields.RegexField(valid_mobile, required=False, help_text=u"收货人电话号码")),
            ('address', fields.CharField(required=True, help_text=u"地址")),
        )

@site
class PartnerGet(CompanyUserApiView):
    """
        合作伙伴公司
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        id = request.params.id

        code, mess, data = user_get_partner_by_id(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'get'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"数据唯一ID")),
        )


@site
class PartnerTerm(CompanyUserApiView):
    """
        合作伙伴公司
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        term = request.params.term

        code, mess, data = get_partner_by_term(user, term)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'term/get'
        param_fields = (
            ('term', fields.CharField(required=False, help_text=u"查询条件")),
        )


urlpatterns = site.urlpatterns