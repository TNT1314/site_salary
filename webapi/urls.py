#! usr/bin/env python
# encoding: utf-8
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
    # 测试接口
    url(r'^test/', include('webapi.apis.rest_view_test')),

    # 用户接口
    url(r'^user/', include('webapi.apis.api_user')),
]
 
