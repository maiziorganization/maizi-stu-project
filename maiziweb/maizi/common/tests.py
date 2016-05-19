#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
import re
# Create your tests here.

def error_message(error):
    way1=r'<ul class="errorlist"><li>(.*?)<ul class="errorlist"><li>(.*?)</li></ul>'
    partens = re.compile(way1,re.S)
    items1 = re.findall(partens,error)
    items1[0][1]

if __name__=='__main__':
    str1 = r'<ul class="errorlist"><li>email<ul class="errorlist"><li>请输入正确的邮箱</li></ul></li></ul>'
    error_message(str1)
