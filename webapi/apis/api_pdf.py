#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-10
    desc: 
        site_salary
"""

import os

from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view

from site_salary.common.apicode import ApiCode
from site_salary.common.backformat import JsonResponse

from website.decorators.userdecorator import NeedCompanyUser, NeverResubmit
from webapi.business.bus_bill_pdf import generate_quarter_salary_pdf


@api_view(["GET"])
@NeedCompanyUser
# @NeverResubmit
def print_bill(request):
    """
        :param request:
        :return:
    """
    user = request.user
    bill_id = request.GET['bill_id']
    bill_type = request.GET['bill_type']

    if bill_id and bill_type:
        if bill_type == 'quarter_salary':
            file_name, binary_pdf = generate_quarter_salary_pdf(user, bill_id)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename="{}.pdf"'.format(file_name)
            response.write(binary_pdf)
        else:
            data = dict()
            code = ApiCode.success.code
            mess = ApiCode.success.mess
            response = HttpResponse(content_type='application/json')
            response.write(JsonResponse(code, mess, data))
    else:
        data = dict()
        code = ApiCode.success.code
        mess = ApiCode.success.mess
        response = HttpResponse(content_type='application/json')
        response.write(JsonResponse(code, mess, data))
    return response
 
