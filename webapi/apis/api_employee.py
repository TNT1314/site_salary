#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
    @version: python2.7.10
    @project_name: site_salary
    @author: wormer(wormer@wormer.cn)
    @date: 17/11/2 00:01
    @description:
        公司雇员接口类
"""

from mixrestview import ViewSite, fields

from .api_base_view import CompanyUserApiView
from site_salary.common.backformat import JsonResponse
from webapi.business.bus_employee import (
    get_employees_pager
)

site = ViewSite(name="employee", app_name="webapi")


@site
class EmployeeList(CompanyUserApiView):
    """
        企业员工列表
    """

    def get_context(self, request, *args, **kwargs):

        name = request.params.name
        phone = request.params.phone
        pagesize = request.params.pagesize
        pagenum = request.params.pagenum
        sortdatafield = request.params.sortdatafield
        sortorder = request.params.sortorder

        code, mess, data = get_employees_pager(pagesize, pagenum, name, phone, sortdatafield, sortorder)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'list/get'
        param_fields = (
            ('pagesize', fields.IntegerField(required=True, help_text=u"页面数据")),
            ('pagenum', fields.IntegerField(required=True, help_text=u"当前页数")),
            ('name', fields.CharField(required=False, help_text=u"员工姓名")),
            ('phone', fields.CharField(required=False, help_text=u"员工电话")),
            ('sortdatafield', fields.CharField(required=False, help_text=u"排序字段")),
            ('sortorder', fields.CharField(required=False, help_text=u"排序方式（asc:升序,des:降序）")),
        )


urlpatterns = site.urlpatterns