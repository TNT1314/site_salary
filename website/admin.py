#! usr/bin/env python
# encoding: utf-8

# Register your models here.

from django.contrib import admin


admin.autodiscover()

# 公司信息
from website.models.company_info import CompanyInfo
admin.site.register(CompanyInfo)


from website.models.company_user import CompanyUser
admin.site.register(CompanyUser)