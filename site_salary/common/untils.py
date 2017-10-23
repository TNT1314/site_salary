#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-10-23
    desc: 
        site_salary
"""


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


if __name__ == '__main__':
    """ do something here """
    pass
 
