#! usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-26
    desc: 
        md5 hash 类
"""

import hashlib
from collections import OrderedDict

from django.contrib.auth.hashers import mask_hash
from django.contrib.auth.hashers import MD5PasswordHasher

__all__ = ['Md5Hash']

class Md5Hash(MD5PasswordHasher):
    algorithm = "md5hash"

    @classmethod
    def encode(cls, password, salt):
        assert password is not None
        hash = hashlib.md5(password).hexdigest().upper()
        return hash

    @classmethod
    def verify(cls, password, encoded):
        encoded_2 = cls.encode(password, '')
        return encoded.upper() == encoded_2.upper()

    def safe_summary(self, encoded):
        return OrderedDict([(_('algorithm'), self.algorithm),(_('salt'), ''),(_('hash'), mask_hash(hash)),])
 
