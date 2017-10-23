#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-12
    desc: 
        site_salary.set_db
        help : https://docs.djangoproject.com/en/1.10/ref/settings/#databases
"""

__all__ = ['DATABASES']

# mysql
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salary',
        'USER': 'builder',
        'PASSWORD': 'ASDasd!@#123',
        'HOST': '127.0.0.1',
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salary',
        'USER': 'builder',
        'PASSWORD': 'ASDasd!@#123',
        'HOST': '127.0.0.1',
    },
}
 
