#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-23
    desc: 
        常用方法类
"""

import socket
from datetime import datetime

from .define import ENUM_IMAGE_PATH
from .md5hash import Md5Hash

def upload_path(instance, filename):
    """
        自定义文件路径问题
        :param instance:
        :param filename:
        :return:
    """
    file_path = list()
    file_path.append(ENUM_IMAGE_PATH.COMPANYUSER)
    file_path.append(str(instance.id))
    file_path.append(filename)
    return '/'.join(file_path)


def get_paging_index(p_size, p_number):
    """
        获取分页下标
        :param p_size:  页面条数
        :param p_number:  页面序号
        :return:
    """
    start = p_size * p_number
    end = p_size * (p_number+1) -1

    return start, end


def password2md5(key, slat):
    """
        字符串MD5加密
        :param key:
        :return:
    """
    return Md5Hash.encode(key, slat)


def get_local_ip():
    """
        获取本机IP
        :return:
    """
    host_ip = '0.0.0.0'
    try:
        web_con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        web_con.connect(('www.baidu.com', 80))
        host_ip = web_con.getsockname()[0]
    except Exception:
        pass
    return host_ip
 
