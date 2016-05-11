#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from maizi.common.views import index,rkSearch

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'rkSearch$',rkSearch,name='rkSearch')
]
