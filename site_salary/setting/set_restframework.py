#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-12
    desc: 
        site_salary
"""

__all__ = ['REST_FRAMEWORK']


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

    'DEFAULT_RENDERER_CLASSES': (
        'mixrestview.apirender.WebApiRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
}
