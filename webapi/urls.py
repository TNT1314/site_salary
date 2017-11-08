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

from django.conf.urls import url, include


urlpatterns = [
    # 企业用户接口类
    url(r'^user/', include('webapi.apis.api_user')),

    # 企业员工接口类
    url(r'^employee/', include('webapi.apis.api_employee')),

    # 企业物料接口类
    url(r'^material/', include('webapi.apis.api_material')),

    # 企业物料定价接口类
    url(r'^process/price/', include('webapi.apis.api_process_price')),

    # 企业季度工资接口类
    url(r'^quarter/salary/', include('webapi.apis.api_quarter_salary')),

    # 测试接口
    url(r'^test/one/', include('webapi.apis.rest_view_test')),

    # 测试接口
    url(r'^test/two/', include('webapi.apis.api_test')),
]
 
