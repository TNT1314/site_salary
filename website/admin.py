#! usr/bin/env python
# -*- encoding: utf-8 -*-

# Register your models here.

from django.contrib import admin


admin.autodiscover()

# 公司信息
from website.models.company_info import CompanyInfo
admin.site.register(CompanyInfo)

# 分组信息
from website.models.group_info import GroupInfo
from website.adminsite.site_group import SiteGroupInfo
admin.site.register(GroupInfo, SiteGroupInfo)

# 用户信息
from website.models.company_user import CompanyUser
admin.site.register(CompanyUser)

# 菜单信息
from website.models.menu_info import MenuInfo
admin.site.register(MenuInfo)

# 分组权限信息
from website.models.group_menu_rel import GroupMenuRel
admin.site.register(GroupMenuRel)

# 用户权限
from website.models.user_menu_rel import UserMenuRel
admin.site.register(UserMenuRel)

# 公司雇员
from website.models.employee_info import EmployeeInfo
admin.site.register(EmployeeInfo)

# 公司物料信息
from website.models.material_info import MaterialInfo
admin.site.register(MaterialInfo)


# 公司物料加工定价信息
from website.models.process_price import ProcessPrice
admin.site.register(ProcessPrice)

# 公司季度工资表
from website.models.quarter_salary import QuarterSalary
admin.site.register(QuarterSalary)

# 公司季度工资表
from website.models.quarter_salary import QuarterSalaryItem
admin.site.register(QuarterSalaryItem)

