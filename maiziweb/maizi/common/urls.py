#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from maizi.common.views import rkSearch,my_login,index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'rkSearch$',rkSearch,name='rkSearch'),
    url(r'my_login$',my_login,name='my_login')
]
