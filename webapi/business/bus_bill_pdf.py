#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-12
    desc: 
        site_salary
"""

import os
from django.conf import settings
from site_salary.common.rml2pdf import RmlPdfUtils
from site_salary.common.define import DICT_QUARTER_ALL

from website.models.quarter_salary import QuarterSalary
from webapi.serializers.set_quarter_salary import S_I_QuarterSalary


def generate_quarter_salary_pdf(user, id):
    """
        根据id 生成季度薪资pdf
    """

    rml_pdf_util = RmlPdfUtils(static_dir=settings.BASE_DIR)

    m_quarter = QuarterSalary.objects.filter(company=user.company, id=int(id)).first()

    save_name = u"{}{}年{}工资明细.pdf".format(m_quarter.employee.name, m_quarter.year, DICT_QUARTER_ALL[m_quarter.quarter])
    save_path = os.path.join(settings.BASE_DIR, 'uploads', 'print', save_name)

    # 获取模版
    template_path = os.path.join(settings.BASE_DIR, 'site_salary', 'templates', 'rml', 'quarter_salary.prep')

    s_quarter = S_I_QuarterSalary(m_quarter)

    binary_pdf = rml_pdf_util.generate_pdf(s_quarter.data, template_path, save_path)

    return save_name, binary_pdf
