#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        site_salary
"""

__all__ = ['NeedAccountUser', 'NeedManagerAccountUser', 'NeverResubmit']

import logging

from functools import wraps

from django.core.cache import cache
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser

from site_salary.common.backformat import JsonResponse
from site_salary.common.apicode import ApiCode
from site_salary.common.backformat import MessResponse
from website.models.company_user import CompanyUser

logger = logging.getLogger('api_view')


def _get_permission(user):
    """
        平台用户验证
        :param user:
        :return: 是否平台用户，及用户类型
    """
    return user.is_authenticated() and isinstance(user, CompanyUser)


def NeedCompanyUser(view, mark=''):
    """
        账号用户修饰器
        :param view:
        :param mark:
        :return:
    """
    @wraps(view)
    def wrap(*args, **kwargs):
        _request = args[0]

        if isinstance(_request.user, AnonymousUser):
            response_context = MessResponse(ApiCode.nopermission.code, ApiCode.nopermission.mess)
            return Response(response_context)
        else:
            if not _get_permission(_request.user):
                response_context = MessResponse(ApiCode.nopermission.code, ApiCode.nopermission.mess)
                return Response(response_context)
            else:
                res_view = view(*args, **kwargs)
                return res_view
    return wrap
 

def NeverResubmit(view):
    @wraps(view)
    def wrap(*args, **kwargs):
        request = args[0]
        key = 'view_never_submit_{}_{}.{}'.format(request.user.id, view.__module__, view.__name__)
        with cache.lock(key):
            if cache.get(key):
                logger.info("u={} f={}".format(request.user, view.__name__))
                response_context = JsonResponse(ApiCode.submitsecond.code, ApiCode.submitsecond.mess, {})
                return Response(response_context)
            cache.set(key, True, 15)
        ret = view(*args, **kwargs)
        cache.delete(key)
        return ret
    return wrap

