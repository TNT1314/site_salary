#! usr/bin/env python
# -*- encoding: utf-8 -*-

# Register your models here.

from django.contrib import admin


admin.autodiscover()

# 公司信息
from website.models.company_info import CompanyInfo
admin.site.register(CompanyInfo)

# 用户信息
from website.models.company_user import CompanyUser
admin.site.register(CompanyUser)

# 菜单信息
from website.models.menu_info import MenuInfo
admin.site.register(MenuInfo)

# 用户权限
from website.models.user_menu_rel import UserMenuRel
admin.site.register(UserMenuRel)

# 分组信息
from website.models.group_info import GroupInfo
admin.site.register(GroupInfo)

# 分组权限信息
from website.models.group_menu_rel import GroupMenuRel
admin.site.register(GroupMenuRel)

# 用户分组信息
from website.models.user_group_rel import UserGroupRel
admin.site.register(UserGroupRel)

