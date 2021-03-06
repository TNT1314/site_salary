#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-02
    desc: 
        site_salary
"""

import re
import string

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, BaseValidator

class ValidateMixin(object):
    """
        Extend Validator a method 'is_valid'
    """

    def is_valid(self, value):
        try:
            self(value)
            return True
        except ValidationError:
            return False


class RegexValidatorPlus(ValidateMixin, RegexValidator):
    pass


class ComplexityValidator(ValidateMixin, BaseValidator):
    min_length = 6
    max_length = 16
    min_types = 3

    char_types = (
        'uppercase', 'lowercase', 'letters', 'digits', 'special', 'punctuation'
    )
    code = 'complexity'
    message = {
        'blanks': u'不能含有空白字符',
        'min_length': u'不能少于%(min_length)d位字符',
        'max_length': u'不能多于%(max_length)d位字符',
        'min_types': u'需要包含大写字母、小写字母、数字、特殊字符中的%(min_types)d种以上类型',
        'default': u'复杂度不能满足要求',
    }

    def __init__(self, **kwargs):
        self.min_types = kwargs.pop('min_types', self.min_length)
        self.min_length = kwargs.pop('min_length', self.min_length)
        self.max_length = kwargs.pop('max_length', self.max_length)

        checking_map = {}
        for char_type in self.char_types:
            checking_map[char_type] = 0

        for k, v in kwargs.iteritems():
            if k not in self.char_types:
                raise TypeError('ComplexityValidator does not support charactor type: %s' % k)
            checking_map[k] = v

        self.checking_map = checking_map

    def __call__(self, value):
        params = self.__dict__.copy()
        if len(value) < self.min_length:
            raise ValidationError(self.message['min_length'], self.code, params)
        if len(value) > self.max_length:
            raise ValidationError(self.message['max_length'], self.code, params)

        checking_map = self.checking_map.copy()
        char_types = set()
        for character in value:
            if character.isupper():
                checking_map['uppercase'] -= 1
                checking_map['letters'] -= 1
                char_types.add('uppercase')
            elif character.islower():
                checking_map['lowercase'] -= 1
                checking_map['letters'] -= 1
                char_types.add('lowercase')
            elif character.isdigit():
                checking_map['digits'] -= 1
                char_types.add('digits')
            elif character in string.punctuation:
                checking_map['punctuation'] -= 1
                checking_map['special'] -= 1
                char_types.add('special')
            elif not character.isspace():
                checking_map['special'] -= 1
                char_types.add('special')
            else:
                raise ValidationError(self.message['blanks'], self.code, params)

        if len(char_types) < self.min_types:
            raise ValidationError(self.message['min_types'], self.code, params)

        for char_type in self.char_types:
            if checking_map[char_type] > 0:
                raise ValidationError(self.message['default'], self.code, params)

# 密码强度
valid_password = ComplexityValidator(min_length=8, max_length=1024, min_types=3)

# 手机号
valid_mobile = RegexValidatorPlus(re.compile('^1[0-9]{10}$'), '手机号格式不正确！')

# 中文
valid_chinese = RegexValidatorPlus(re.compile('^[\u4e00-\u9fa5]*$'), '含有非中文字符！')

# 身份证号
valid_identity = RegexValidatorPlus(re.compile(
        '^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$'
    ),
    '身份证格式不正确！'
)

# 数字判断
valid_int = RegexValidatorPlus(re.compile('^\+?[1-9][0-9]*$'), '验证是否为数字！')

# 邮箱判断
valid_email = RegexValidatorPlus(
    re.compile('^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'),
    '邮箱格式不正确！')

# 社会信用代码
valid_social = RegexValidatorPlus(
    re.compile('^[1-9A-GY]{1}[1239]{1}[1-5]{1}[0-9]{5}[0-9A-Z]{10}$'),
    '公司统一信用代码不正确！')

valid_char = RegexValidatorPlus(re.compile('^[a-zA-Z]+$'), '字符串格式不正确！')

# 验证年份
valid_year = RegexValidatorPlus(re.compile('^[2-3]+\d{3}$'), '请填写正确的年份 ！')

# 验证座机号码
valid_tell = RegexValidatorPlus(re.compile('^(0[0-9]{2,3}/-)?([2-9][0-9]{6,7})+(/-[0-9]{1,4})?$'), '请填写争取的座机号码！')
 
