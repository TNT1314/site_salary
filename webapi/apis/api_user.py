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

from mixrestview import ViewSite, fields
from site_salary.common.baseapiview import UserApiView
from webapi.business.b_user import get_user_by_params


site = ViewSite(name="user", app_name="webapi")


@site
class UserListGet(UserApiView):

    """
        接口说明部分
    """

    def get_context(self, request, *args, **kwargs):
        p_size = request.params.pagesize
        p_numb = request.params.pagenum
        username = request.params.username
        email = request.params.email
        sortdatafield = request.params.sortdatafield
        sortorder = request.params.sortorder

        result = get_user_by_params(p_size, p_numb, username, email, sortdatafield, sortorder)

        return result

    class Meta:
        path = 'list/get'
        param_fields = (
            ('pagesize', fields.IntegerField(required=True, help_text=u"页面数据")),
            ('pagenum', fields.IntegerField(required=True, help_text=u"当前页数")),
            ('username', fields.CharField(required=False, help_text=u"登录用户")),
            ('email', fields.CharField(required=False, help_text=u"邮件地址")),
            ('sortdatafield', fields.CharField(required=False, help_text=u"排序字段")),
            ('sortorder', fields.CharField(required=False, help_text=u"排序方式（asc:升序,des:降序）")),
        )

urlpatterns = site.urlpatterns
