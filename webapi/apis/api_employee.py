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
from site_salary.common.regular import (
    valid_email, valid_mobile
)
from site_salary.common.define import (
    LIST_EMPLOYEE_STATUS,LIST_EMPLOYEE_GENDER
)
from webapi.business.bus_employee import (
    user_get_employees_pager, user_get_employee_by_id,
    user_add_employee, user_update_employee
)

site = ViewSite(name="employee", app_name="webapi")


@site
class EmployeeList(CompanyUserApiView):
    """
        企业员工列表
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        name = request.params.name
        phone = request.params.phone
        pagesize = request.params.pagesize
        pagenum = request.params.pagenum
        sortdatafield = request.params.sortdatafield
        sortorder = request.params.sortorder

        code, mess, data = user_get_employees_pager(user, pagesize, pagenum, name, phone, sortdatafield, sortorder)

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

@site
class EmployeeGet(CompanyUserApiView):
    """
        企业员工列表
    """

    def get_context(self, request, *args, **kwargs):

        id = request.params.id
        user = request.user

        code, mess, data = user_get_employee_by_id(user,id)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'get'
        param_fields = (
            ('id', fields.IntegerField(required=True, help_text=u"唯一ID")),
        )

@site
class EmployeeChange(CompanyUserApiView):
    """
        添加企业员工
    """

    def get_context(self, request, *args, **kwargs):

        user = request.user
        name = request.params.name
        phone = request.params.phone
        gender = request.params.gender
        email = request.params.email
        status = request.params.status
        address = request.params.address

        id = request.params.id

        if id:
            code, mess, data = user_update_employee(user, id, name, phone, gender, email, status, address)
        else:
            code, mess, data = user_add_employee(user,name, phone, gender, email, status, address)

        return JsonResponse(code, mess, data)

    class Meta:
        path = 'change'
        param_fields = (
            ('id', fields.CharField(required=False, help_text=u"修改某个员工的唯一标识")),
            ('name', fields.CharField(required=True, help_text=u"新增员工的姓名")),
            ('phone', fields.RegexField(required=True, regex=valid_mobile, help_text=u"新增员工的联系电话")),
            ('gender', fields.ChoiceField(required=True, choices=LIST_EMPLOYEE_GENDER, help_text=u"新增员工的性别")),
            ('email', fields.RegexField(required=False, regex=valid_email, help_text=u"新增员工的电子邮箱")),
            ('status', fields.ChoiceField(required=True, choices=LIST_EMPLOYEE_STATUS, help_text=u"新增员工的状态")),
            ('address', fields.CharField(required=False, help_text=u"新增员工的家庭住址")),
        )

urlpatterns = site.urlpatterns