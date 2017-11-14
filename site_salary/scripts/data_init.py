#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-07
    desc: 
        site_salary
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_salary.settings")
django.setup()

from django.db import transaction
from website.models.menu_info import MenuInfo
from website.models.group_info import GroupInfo
from website.models.company_user import CompanyUser
from website.models.group_menu_rel import GroupMenuRel
from website.models.company_info import CompanyInfo

MENUS = [
    {"code": "JCXX", "name": u"基础信息", "icon": "fa-globe", "model": "", "desc": u"系统基础信息", "parent": ""},
    {"code": "WLXX", "name": u"物料信息", "icon": "fa-chain", "model": "material", "desc": u"基础物料资料管理", "parent": "JCXX"},
    {"code": "RLZY", "name": u"人力资源", "icon": "fa-users", "model": "", "desc": u"人力资源模块", "parent": ""},
    {"code": "RYXX", "name": u"人员信息", "icon": "fa-user", "model": "employee", "desc": u"企业人员管理", "parent": "RLZY"},
    {"code": "GJDJ", "name": u"工件定价", "icon": "fa-steam", "model": "processprice", "desc": u"加工工件计件价格管理", "parent": "RLZY"},
    {"code": "JDGZ", "name": u"季度工资", "icon": "季度工资", "model": "quartersalary", "desc": u"季度工件计件工资管理", "parent": "RLZY"}
]


def init_menus():
    """
        :return:
    """
    try:
        with transaction.atomic():
            for menu in MENUS:
                q_menu = MenuInfo.objects.filter(code=menu['code'])
                if not q_menu.exists():
                    m_menu = MenuInfo()
                    m_menu.code = menu['code']
                    m_menu.name = menu['name']
                    m_menu.icon = menu['icon']
                    m_menu.model = menu['model']
                    m_menu.desc = menu['desc']

                    if menu['parent']:
                        p_menu = MenuInfo.objects.filter(code=menu['parent'])

                        if p_menu:
                            m_menu.parent = p_menu.first()
                    m_menu.save()
        print "init_menus success."
    except Exception as e:
        print "init_menus error. {}".format(e)



COMPANYS = [
    {"code": "HBSFCXGDJXC", "name": u"河北省阜城县国栋机械厂", "shot_name": u"国栋机械厂", "license":"131128600034813", "address": u"河北省阜城县古城镇西火星堂村1号"}
]


def init_company():
    """
        初始化公司信息
    """
    try:
        for company in COMPANYS:
            q_company= CompanyInfo.objects.filter(code=company['code'])
            if not q_company.exists():
                m_compay = CompanyInfo()
                m_compay.code = company['code']
                m_compay.name = company['name']
                m_compay.shot_name = company['shot_name']
                m_compay.license = company['license']
                m_compay.address = company['address']
                m_compay.save()
        print "init_company success."
    except Exception as e:
        print "init_company error. {}".format(e)
        

GROUPS = [
    {"code": "HBSFCXGDJXCZ", "name":"河北省阜城县国栋机械厂组", "desc": u"河北省阜城县国栋机械厂权限列表"}
]


def init_group():
    """
        初始化分组
    """
    try:
        for group in GROUPS:
            q_group = GroupInfo.objects.filter(code=group['code'])
            if not q_group.exists():
                m_group = GroupInfo()
                m_group.code = group['code']
                m_group.name = group['name']
                m_group.desc = group['desc']
                m_group.save()
        print "init_group success."
    except Exception as e:
        print "init_group error. {}".format(e)


GROUP_MENUS = {
    "HBSFCXGDJXCZ": [
        {"menu_code": "RLZY", "p_inf": True, "p_add":True, "p_cha":True, "p_aud":False, "p_del":False, "p_pri": False},
        {"menu_code": "RYXX", "p_inf": True, "p_add":True, "p_cha":True, "p_aud":False, "p_del":False, "p_pri": False},
        {"menu_code": "GJDJ", "p_inf": True, "p_add":True, "p_cha":True, "p_aud":False, "p_del":False, "p_pri": False},
        {"menu_code": "JDGZ", "p_inf": True, "p_add":True, "p_cha":True, "p_aud":True, "p_del":False, "p_pri": True},
    ]
}


def init_group_menus():
    """
        初始化分组权限
    """

    try:
        for key in GROUP_MENUS:
            q_group = GroupInfo.objects.filter(code=key)

            if q_group.first():
                m_group = q_group.first()
                with transaction.atomic():
                    menus = GROUP_MENUS[key]
                    for menu in menus:
                        q_menu = MenuInfo.objects.filter(code=menu["menu_code"])
                        if q_menu.first():
                            m_menu = q_menu.first()
                            q_rel = GroupMenuRel.objects.filter(group=m_group, menu=m_menu)
                            if not q_rel.exists():
                                q_group_menu = GroupMenuRel()
                                q_group_menu.group = m_group
                                q_group_menu.menu = m_menu
                                q_group_menu.p_inf = menu['p_inf']
                                q_group_menu.p_add = menu['p_add']
                                q_group_menu.p_cha = menu['p_cha']
                                q_group_menu.p_aud = menu['p_aud']
                                q_group_menu.p_del = menu['p_del']
                                q_group_menu.p_pri = menu['p_pri']
                                q_group_menu.save()
        print "init_group_menus success."
    except Exception as e:
        print "init_group_menus error. {}".format(e)


COMPANY_USERS = [
    {"company": "HBSFCXGDJXC", "username": "guodongjixie", "password": "ASDasd!@#123",
     "name": u"刘美", "mobile": "18810958549", "email": "liumei@wormer.cn", "avatar": "", "group": "HBSFCXGDJXCZ"}
]


def init_company_user():
    """
        初始化公司用户
        :return:
    """
    try:
        for user in COMPANY_USERS:
            q_company = CompanyInfo.objects.filter(code=user["company"])

            if q_company.first():
                m_company = q_company.first()
                q_group = GroupInfo.objects.filter(code=user["group"])
                m_group = q_group.first()

                q_company_user = CompanyUser.objects.filter(company=m_company, username=user["username"])

                if not q_company_user.exists():
                    m_company_user = CompanyUser()
                    m_company_user.company = m_company
                    m_company_user.group = m_group
                    m_company_user.username = user["username"]
                    m_company_user.password = user["password"]
                    m_company_user.name = user["name"]
                    m_company_user.mobile = user["mobile"]
                    m_company_user.email = user["email"]
                    m_company_user.avatar = user["avatar"]
                    m_company_user.save()
        print "init_company_user success."
    except Exception as e:
        print "init_company_user error. {}".format(e)


if __name__ == '__main__':
    init_menus()
    init_company()
    init_group()
    init_group_menus()
    init_company_user()


