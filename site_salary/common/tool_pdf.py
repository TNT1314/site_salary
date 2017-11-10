#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: liujun
    proj: firefighting_map
    date: 2017-05-31
    desc: firefighting_map
"""

import os
import logging
import StringIO
from PIL import Image
from django.conf import settings
from site_salary.common.tool_rml2pdf import PdfUtils
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A3, landscape

logger = logging.getLogger("")

def change_size(image_file, page_w, page_h):
    """
        根据实际高度获得偏移
        :param page_w:
        :param page_h:
        :param img_w:
        :param img_h:
        :return:
    """
    offset_x, offset_y = 0, 0

    # 高度计算

    # 以宽度计算
    if page_w < image_file.width:
        new_w = image_file.width
        new_h = image_file.height * (page_w / image_file.width)

        offset_y = (page_h - new_h) / 2
        image_file.thumbnail((new_w, new_h), Image.ANTIALIAS)
    return image_file, offset_x, offset_y


def draw_image2pdf(imagechar, filename):
    try:
        image_file_dir = '{}reduce'.format(settings.MEDIA_ROOT)

        if not os.path.exists(image_file_dir):
            os.makedirs(image_file_dir)
        # # 横向输出
        # image_canvas = Canvas(
        #     'uploads/pdf/{}.pdf'.format(filename),
        #     pageCompression=False,
        #     invariant=True,
        #     bottomup=1,
        #     pagesize=landscape(A3)
        # )
        #
        # page_height, page_width = landscape(A3)
        #
        # image_file, offset_x, offset_y = change_size(image_file, page_height, page_width)
        #
        # image_canvas.drawInlineImage(
        #     image_file, offset_x, offset_y, width=image_file.width, height=image_file.height, preserveAspectRatio=True
        # )
        #
        # image_canvas.showPage()
        # image_canvas.save()
        image_file = Image.open(StringIO.StringIO(imagechar))

        image_file_path = "{}/{}.png".format(image_file_dir, filename)
        image_file.save(image_file_path, "PNG")
    except Exception as e:
        logger.error(e)
    return True, "/media/reduce/{}.png".format(filename)



def genarate_firesafetybill_pdf(user, id):
    """
        根据ID获取消防工单生成pdf
        :param user:
        :param id:
        :return:
    """

    create_pdf = PdfUtils()

    tem_path = os.path.join(settings.BASE_DIR, 'firefighting_map', 'templates', 'rml', 'firesafetyprint.prep')

    binary_pdf = create_pdf.generate_local_pdf({}, tem_path, save_file=None)

    return binary_pdf