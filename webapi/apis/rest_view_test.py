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
 
from mixrestview import ViewSite, fields, validators
from site_salary.common.baseapiview import SalaryApiView


site = ViewSite(name="test", app_name="webapi")


@site
class AppPing(SalaryApiView):
    """
        接口说明部分
    """

    def get_context(request, *args, **kwargs):

        result = dict()
        result['code'] = '10000'
        result['mesg'] = 'success'
        return result

    class Meta:
        path = 'ping'
        param_fields = (
            ('carno', fields.CharField(required=True, help_text=u"文本")),
            ('int', fields.IntegerField(required=True, help_text=u"数字")),
            ('boolean', fields.BooleanField(required=True, help_text=u"布尔值")),
            ('float', fields.FloatField(required=True, help_text=u"浮点型")),
            ('date', fields.DateField(required=True, help_text=u"日期")),
            ('image', fields.ImageField(required=True, help_text=u"图片")),
            ('deciminal', fields.DecimalField(required=True, max_digits=4, decimal_places=10, help_text=u"浮点型")),
            ('indentity', fields.RegexField(required=True, regex=validators.valid_identity, help_text=u"正则表达式")),

        )


urlpatterns = site.urlpatterns