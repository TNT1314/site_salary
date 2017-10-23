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

from rest_framework.validators import UniqueTogetherValidator
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListUsers(APIView):
    """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
            Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


if __name__ == '__main__':
    """ do something here """
    pass
 
