#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-14
    desc: 
        site_salary
"""
__all__ = ['ImageCodeUtil']

import os
import random
import base64
import cStringIO

from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(1, 10)))  # 数字
RANDOM_CHARS = ''.join((_upper_cases, _numbers))


class ImageCodeUtil(object):
    """
        图形验证码工具

    """

    def __init__(self,
                 size=(120, 30),
                 length=4,
                 image=("RGB", "PNG"),
                 colors=((0, 0, 255), (255, 255, 255)),
                 font=("ae_AlArabiya.ttf", 18),
                 line=(True, (2, 3)),
                 point=(True, 2)):
        """
            :param size: (width, height)
            :param image_type: ("RGB", "PNG")
            :param colors: ((0, 0, 255), (255, 255, 255),)
            :param font: ("ae_AlArabiya.ttf",18)
            :param line:
            :param point:
        """

        self.chars = RANDOM_CHARS
        self.width = size[0]
        self.height = size[1]
        self.length = length
        self.img_mode = image[0]
        self.img_type = image[1]
        self.color_fore = colors[0]
        self.color_back = colors[1]
        self.font_type = font[0]
        self.font_size = font[1]
        self.line_has = line[0]
        self.line_range = line[1]
        self.point_has = point[0]
        self.point_range = point[1]

    def random_chars(self):
        """
            生成给定长度的字符串，返回列表格式
            :return:
        """
        return random.sample(self.chars, self.length)

    def random_color(self):
        """
            随机颜色
        """
        one = random.randint(0, 255)
        two = random.randint(0, 255)
        three = random.randint(0, 255)
        return (one, two, three)

    def draw_lines(self, draw):
        """
            绘制干扰线
            :return:
        """
        line_num = random.randint(*self.line_range)  # 干扰线条数

        for i in range(line_num):
            half_width = int(self.width)/2
            half_height = int(self.height)/2
            # 起始点
            line_begin = (random.randint(0, half_width), random.randint(0, half_height))
            # 结束点
            line_end = (random.randint(half_width, self.width), random.randint(half_height, self.height))
            draw.line([line_begin, line_end], fill=self.random_color())

    def draw_points(self, draw):
        """
            绘制干扰点
            :return:
        """
        point_num = min(100, max(0, int(self.point_range)))  # 大小限制在[0, 100]

        for w in xrange(self.width):
            for h in xrange(self.height):
                tmp = random.randint(0, 100)
                if tmp > 100 - point_num:
                    draw.point((w, h), fill=self.random_color())

    def draw_chars(self, draw):
        """
            绘制验证码字符
        """
        random_chars = self.random_chars()
        code_chars = ' %s ' % ' '.join(random_chars)  # 每个字符前后以空格隔开
        try:
            draw_font = ImageFont.truetype(str(self.font_type), self.font_size)
        except:
            font_file = "{}/pdf_fonts/Menlo.ttc".format(os.path.split(os.path.realpath(__file__))[0])
            draw_font = ImageFont.truetype(str(font_file), self.font_size)
        font_width, font_height = draw_font.getsize(code_chars)
        draw.text(((self.width - font_width) / 3, (self.height - font_height) / 3), code_chars, font=draw_font, fill=self.color_fore)
        return ''.join(random_chars)

    def generate_image4code(self):
        """
            绘制图片
            :return:
        """
        img4code = Image.new(self.img_mode, (self.width, self.height), self.color_back)  # 创建图形
        # 创建画笔
        draw = ImageDraw.Draw(img4code)
        # 画干扰点
        self.draw_points(draw)
        # 划线
        self.draw_lines(draw)
        # 画随机编码
        random_code = self.draw_chars(draw)

        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100, 0, 0, 0, 1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500, 0.001, float(random.randint(1, 2)) / 500
                  ]
        # 创建扭曲
        img4code = img4code.transform((self.width,self.height), Image.PERSPECTIVE, params)
        # 滤镜，边界加强（阈值更大）
        img4code = img4code.filter(ImageFilter.EDGE_ENHANCE_MORE)

        return img4code, random_code

    def generate_base64_image4code(self):
        """
            生成base64位二进制流
            :return:
        """
        buffer = cStringIO.StringIO()

        image_file, random_code = self.generate_image4code()

        image_file.save(buffer, format=self.img_type)

        base64_str = base64.b64encode(buffer.getvalue())

        return base64_str, random_code


if __name__ == "__main__":
    code_img, chars = ImageCodeUtil().generate_image4code()
    code_img.save("validate.png", "PNG")
    print chars
