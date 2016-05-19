#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from maizi.common.views import rkSearch,my_login,index,lesson,register_email,register_phone

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'rkSearch$',rkSearch,name='rkSearch'),
    url(r'my_login$',my_login,name='my_login'),
    url(r'lesson$',lesson,name='lesson'),
    url(r'register_email',register_email,name='register_email'),
    url(r'register_phone',register_phone,name='register_phone'),
]
