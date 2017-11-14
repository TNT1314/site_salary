#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-10
    desc: 
        site_salary
"""

import os
import django
from site_salary.common.smtp import send_email

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_salary.settings")
django.setup()

if __name__ == '__main__':
    """ do something here """
    send_email('wormer@wormer.cn', "hello test", "this is the test file")
