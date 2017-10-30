#! usr/bin/env python
# -*- encoding: utf-8 -*-

"""site_salary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls import url,include


# 屏蔽查看站点
admin.site.site_url = None


urlpatterns = [
    # grappelli url
    url(r'^grappelli/', include('grappelli.urls')),  # new:grap pelli URLS

    # admin url
    url(r'^admin/', admin.site.urls),

    # rest_framework url
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # rest_framework url
    url(r'^api/', include('webapi.urls', namespace='webapi')),

    url( r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_URL}),

    # media url
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]
