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

from site_salary.common.tool_rml2pdf import PdfUtils
from website.decorators.userdecorator import NeedCompanyUser, NeverResubmit

from site_salary.common.tool_pdf import genarate_firesafetybill_pdf


@api_view(["GET"])
@NeedCompanyUser
def pdf_test(request):

    response = HttpResponse(content_type='application/pdf')

    pdf_data = {}

    pdf_util = PdfUtils()

    # 模板页面地址
    tem_path = os.path.join(settings.BASE_DIR, 'firefighting_map', 'templates', 'firesafety', 'bill.prep')

    binary_pdf = pdf_util.generate_binary_pdf(pdf_data, tem_path)

    response.write(binary_pdf)

    return response


@api_view(["GET"])
@NeedCompanyUser
@NeverResubmit
def print_firesafety_bill(request):
    """
        :param request:
        :return:
    """
    user = request.user
    id = request.GET['id']

    binary_pdf = genarate_firesafetybill_pdf(user, id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="消防工单打印.pdf"'
    response.write(binary_pdf)

    return response
 
