#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-08
    desc: 
        site_salary
"""

from mixrestview import ViewSite, fields

from .api_base_view import CompanyUserApiView
from site_salary.common.backformat import JsonResponse
from site_salary.common.define import (
    LIST_QUARTER_ALL
)
from webapi.business.bus_quarter_salary import (
    user_get_quarter_salary_pager, user_get_quarter_salary
)
from webapi.business.bus_process_price import (
    user_get_process_price_pager, user_get_process_price,
    user_add_process_price, user_update_process_price
)


site = ViewSite(name="quarter_salary", app_name="webapi")


@site
class QuarterSalaryList(CompanyUserApiView):
    """
        雇员工资表
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user

        year = request.params.year
        quarter = request.params.quarter
        name = request.params.name

        pagesize = request.params.pagesize
        pagenum = request.params.pagenum
        sortdatafield = request.params.sortdatafield
        sortorder = request.params.sortorder

        code, mess, data = user_get_quarter_salary_pager(
            user, pagesize, pagenum, sortdatafield, sortorder,
            year, quarter, name
        )
        return JsonResponse(code, mess, data)

    class Meta:
        path = 'list/get'
        param_fields = (
            ('pagesize', fields.IntegerField(required=True, help_text=u"页面数据")),
            ('pagenum', fields.IntegerField(required=True, help_text=u"当前页数")),
            ('sortdatafield', fields.CharField(required=False, help_text=u"排序字段")),
            ('sortorder', fields.CharField(required=False, help_text=u"排序方式（asc:升序,des:降序）")),

            ('year', fields.CharField(required=False, help_text=u"年份")),
            ('quarter', fields.ChoiceField(required=False, choices=LIST_QUARTER_ALL, help_text=u"季度")),
            ('name', fields.CharField(required=False, help_text=u"雇员姓名")),
        )


@site
class QuarterSalaryGet(CompanyUserApiView):
    """
        获取物料定价详细信息接口
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        id = request.params.id

        code, mess, data = user_get_quarter_salary(user, id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'get'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"季度工资唯一ID")),
        )


urlpatterns = site.urlpatterns

