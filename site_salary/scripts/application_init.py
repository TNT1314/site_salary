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


def init_data():
    """
        :return:
    """
    print "what's the fucker."


if __name__ == '__main__':
    init_data()



