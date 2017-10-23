#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-12
    desc: 
        site_salary.logging
"""

import os

__all__ = ['LOGGING']

log_path= os.path.abspath(os.path.join(__file__, '../../../logs/django'))

if not os.path.exists(log_path):
    os.makedirs(log_path)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s.%(msecs).03d] %(levelname)s [%(module)s:%(funcName)s:%(lineno)d]- %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        # 记录到日志文件(需要创建对应的目录，否则会出错)
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'default.log'),  # 日志输出文件
            'maxBytes': 1024*1024*5,   # 文件大小
            'backupCount': 5,   # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['debug', 'mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'api_view': {
            'handlers': ['debug', 'mail_admins', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
