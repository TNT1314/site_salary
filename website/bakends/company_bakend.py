#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        site_salary
"""


#! usr/bin/env python
# encoding: utf-8
"""
    用户自动登录方法
"""

import logging

from site_salary.common.md5hash import Md5Hash

from website.models.company_user import CompanyUser

class CompanyUserBackend(object):

    logger = logging.getLogger('authenticate')

    def authenticate(self, username=None, password=None):
        try:

            m_com_user = CompanyUser.objects.get(username=username)

        except Exception as ex:

            self.logger.info('User:{} PassWord:{} Login Exception: {}.'.format(username, password, ex))

            m_com_user = None

        if m_com_user:

            if Md5Hash.verify(password, m_com_user.password):

                self.logger.info('User:{} Login Success.'.format(username))

            else:

                m_com_user = None

                self.logger.info('User:{} PassWord:{} Login Fail.'.format(username, password))

        return m_com_user

    def get_user(self, user_id):
        """
            获取用户
            :param user_id: 主键ID
            :return:
        """
        try:

            m_com_user = CompanyUser.objects.get(id=user_id)

            return m_com_user

        except Exception as ex:

            self.logger.info(u'获取用户(pk={})异常({})！'.format(user_id, ex))

            return None
