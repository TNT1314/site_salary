#! usr/bin/env python
# encoding: utf-8
"""
    third api 邮件接口访问
"""

import logging
from django.conf import settings
from django.utils.encoding import force_bytes
from django.core.mail.message import EmailMultiAlternatives


def send_email(emails, email_title, email_content):
    """
        发送邮件接口
        :param subject:
        :param add_to:
        :param html_content:
        :return:
    """

    logger = logging.getLogger("third_party")

    email_addr = list()

    if isinstance(emails, basestring):
        email_addr.append(emails.decode('utf8'))
    elif isinstance(emails, list):
        email_addr.extend(emails)
    elif isinstance(emails, tuple):
        emails_list = list(emails)
        email_addr.extend(emails_list)

    if isinstance(email_title, str):
        email_title = email_title.decode('utf8')

    if email_title.find(settings.EMAIL_SUBJECT_PREFIX) < 0:
        email_title = settings.EMAIL_SUBJECT_PREFIX + email_title

    mulit_email = EmailMultiAlternatives(
        email_title,
        email_content,
        settings.EMAIL_HOST_USER,
        email_addr
    )
    mulit_email.attach_alternative(email_content, "text/html")
    try:
        mulit_email.send()
        logger.debug(u"SMTP Emails:{} Title:{} Content:{} ".format(email_addr, email_title, email_content))
    except Exception as e:
        logger.error(u"SMTP Emails:{} Title:{} Content:{} Exception: {}".format(email_addr, email_title, email_content, e))
        raise e


def report_exception(msg, *args, **kwargs):
    """
        报错邮件发送
    """
    exc_logger = logging.getLogger('exception')
    exc_logger.exception(msg, *args, **kwargs)
