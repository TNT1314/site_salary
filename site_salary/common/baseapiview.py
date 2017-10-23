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

import logging
from mixrestview.apiview import APIView


class SalaryApiView(APIView):

    logger = logging.getLogger("api_view")


class UserApiView(APIView):

    logger = logging.getLogger("api_view")
