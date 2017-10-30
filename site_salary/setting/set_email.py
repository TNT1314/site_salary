#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-27
    desc: 
        site_salary
"""

__all__ = [
    'SERVER_IP_FILE', 'SERVER_IP', 'EMAIL_SUBJECT_PREFIX',
    'EMAIL_BACKEND', 'EMAIL_USE_TLS', 'EMAIL_HOST',
    'EMAIL_PORT', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD',
    'DEFAULT_FROM_EMAIL', 'SEND_BROKEN_LINK_EMAILS',
    'SERVER_EMAIL', 'MANAGERS'
]

import os
import tempfile

from django.conf import settings
from site_salary.common.untils import get_local_ip

SERVER_IP_FILE = os.path.join(tempfile.gettempdir(), 'server_ip')

try:
    with open(SERVER_IP_FILE, 'rb') as _f:
        SERVER_IP = _f.read().strip()
except IOError:
    SERVER_IP = get_local_ip()
    try:
        with open(SERVER_IP_FILE, 'wb') as _f:
            _f.write(SERVER_IP)
    except IOError, exp:
        import warnings
        warnings.warn("SERVER_IP_FILE could not be accept: %s" % exp)

# 邮箱配置
if not settings.DEBUG:
    EMAIL_SUBJECT_PREFIX = u'WormerErp[P:{}]'.format(SERVER_IP)
else:
    EMAIL_SUBJECT_PREFIX = u'WormerErp[T:{}]'.format(SERVER_IP)


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_HOST = "smtp.wormer.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "master@wormer.cn"
EMAIL_HOST_PASSWORD = "ASDasd!@#123"
DEFAULT_FROM_EMAIL = "master@wormer.cn"


SEND_BROKEN_LINK_EMAILS = True
SERVER_EMAIL = EMAIL_HOST_USER
MANAGERS = ADMINS = (('Admins', 'wormer@wormer.cn'),)
