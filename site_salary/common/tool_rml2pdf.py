#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: liujun
    proj: firefighting_map
    date: 2017-06-27
    desc: firefighting_map
"""

import sys
sys.path.append('/Users/liujun/builder_projects/firefighting_map/')

import os
import preppy
import logging
import traceback
import trml2pdf
from django.conf import settings
from site_salary.settings import BASE_DIR

import reportlab.lib.styles
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib.fonts import addMapping

pdf_logger = logging.getLogger('pdf')


class PdfUtils(object):

    """
        PDF 生成工具类
        将一个标准的RML文件正常解析为PDF文件，保存并返回。具体参数如下
    """

    def __init__(self, font_dir=os.path.join(settings.BASE_DIR, 'static', 'fonts'), static_dir=settings.BASE_DIR):
        """
            构造方法
            @param font_dir 需要注册的字体文件目录
            @param static_dir 静态文件地址目录
        """

        super(PdfUtils, self).__init__()

        self.statics_path = static_dir

        try:
            # 注册宋体字体
            pdfmetrics.registerFont(ttfonts.TTFont('song', os.path.join(font_dir, 'STSONG.TTF')))
            # 注册宋体粗体字体
            pdfmetrics.registerFont(ttfonts.TTFont('song_b', os.path.join(font_dir, 'STZHONGS.TTF')))
        except Exception as e:
            pdf_logger.error(e)
            pdf_logger.error(traceback.format_exc())

        addMapping('song', 0, 0, 'song')     # normal
        addMapping('song', 0, 1, 'song')     # italic
        addMapping('song', 1, 1, 'song_b')   # bold, italic
        addMapping('song', 1, 0, 'song_b')   # bold

        # 设置自动换行
        reportlab.lib.styles.ParagraphStyle.defaults['wordWrap'] = "CJK"

    def generate_local_pdf(self, data, template, save_file):
        """
            从二进制流中创建PDF并返回
            @param data  渲染XML的数据字典
            @param template 需要渲染的XML文件地址（全路径）
            @param save_file PDF文件保存的地址（全路径）
        """

        if not os.path.exists(save_file):
            file_path_array = save_file.split("/")
            save_file_dir = file_path_array[:-1]

            if not os.path.exists("/".join(save_file_dir)):
                os.makedirs("/".join(save_file_dir))

        # 读取模板文件
        m_template = preppy.getModule(template)

        # 渲染模板文件
        render_data = {'data': data, 'STATIC_DIR': self.statics_path}

        # 渲染PDF页面
        char_rml = m_template.getOutput(render_data)

        # 生成PDF
        pdf_binary = trml2pdf.parseString(char_rml)

        # 保存PDF
        open(save_file, 'wb').write(pdf_binary)

        return pdf_binary

    def generate_binary_pdf(self, data, template):
        """
            从二进制流中创建PDF并返回
            @param data  渲染XML的数据字典
            @param template 需要渲染的XML文件地址（全路径）
        """

        # 读取模板文件
        m_template = preppy.getModule(template)

        # 渲染模板文件
        render_data = {'data': data, 'STATIC_DIR': self.statics_path}

        # 渲染PDF页面
        char_rml = m_template.getOutput(render_data)

        # 生成PDF
        pdf_binary = trml2pdf.parseString(char_rml)

        return pdf_binary


if __name__ == '__main__':

    pdf_util = PdfUtils()

    pdf_data = {}

    # 模板页面地址
    tem_path = os.path.join(settings.BASE_DIR, 'firefighting_map', 'templates', 'firesafety', 'bill.prep')

    # 输出地址
    out_path = os.path.join(settings.BASE_DIR, 'downloads', 'firesafetybill', 'product.pdf')

    # 如果PDF不存在则重新生成
    pdf_util.generate_local_pdf(pdf_data, tem_path, out_path)

    print 'done'