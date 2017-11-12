#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-13
    desc: 
        site_salary
"""

__all__ = [
    'BaseApiView', 'SalaryApiView', 'UserApiView','CompanyUserApiView'
]

import logging

from mixrestview.apiview import APIView
from rest_framework.response import Response


from site_salary.common.smtp import report_exception
from site_salary.common.apicode import ApiCode
from site_salary.common.backformat import JsonResponse
from website.decorators.userdecorator import NeedCompanyUser


class BaseApiView(APIView):
    """
        定义日志参数
    """
    logger = logging.getLogger("api_view")

    def handle_exception(self, exc):
        report_exception("500")
        return Response(exc.message) if exc.message else Response(exc.args)


class UserApiView(BaseApiView):
    pass


class SalaryApiView(BaseApiView):
    pass


class CompanyUserApiView(BaseApiView):
    """
        定义公司用户装饰器
    """

    class Meta:
        decorators = [NeedCompanyUser]
