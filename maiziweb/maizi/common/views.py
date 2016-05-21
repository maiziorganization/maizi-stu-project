#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render, redirect, HttpResponse
from models import Ad, Course, RecommendKeywords, CareerCourse, UserProfile
from django.conf import settings
from form import *
from django.contrib.auth import logout, login, authenticate
from django.core.serializers import serialize
import json
import re
from django.views.decorators.csrf import csrf_exempt
import pdb
import logging
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
#开源地址
#https://github.com/shenjiawei19/maizi-stu-project
logger = logging.getLogger('maizi.common.views')

#提取错误信息
def error_message(error):
    way1=r'<ul class="errorlist"><li>(.*?)<ul class="errorlist"><li>(.*?)</li></ul>'
    error_info = re.compile(way1, re.S)
    items = re.findall(error_info, error)
    return items[0][1]


def global_setting(request):
    # 站点基本信息
    SITE_KEY = settings.SITE_KEY
    #站点地址
    SITE_URL = settings.SITE_URL
    #站点主题
    SITE_NAME = settings.SITE_NAME
    #站点描述
    SITE_DESC = settings.SITE_DESC
    #站点推荐搜索关键词
    RecKey = RecommendKeywords.objects.all()
    #所有课程信息
    AllCourse = CareerCourse.objects.all()
    #登入表单信息
    login_form = loginForm()
    #邮箱注册表单信息
    register_email = registerEmailForm()
    #手机注册表单信息
    register_phone = registerMobileForm()
    #密码找回
    reg_password = RgForm()
    return locals()

#首页
def index(request):
    ad_list = Ad.objects.all()
    course_list = Course.objects.all()
    return render(request, "common/index.html", locals())

#点击登入
@csrf_exempt
def my_login(request):
    reason = {"error": ""}
    if request.method == "POST":
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = UserProfile.objects.get(username=username)
                print user.username
                print user.check_password(password)
                if user.check_password(password) is True:
                    reason["username"] = username
                    return HttpResponse(json.dumps(reason), content_type="application/json")
                else:
                    reason["error"]= "账号或密码错误，请重新输入"
                    return HttpResponse(json.dumps(reason), content_type="application/json")
            except:
            # user = authenticate(username=username, password=password)
            # if user is not None:
            #     # user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
            #     # login(request,user)
            #     reason["username"] = username
            #     return HttpResponse(json.dumps(reason), content_type="application/json")
            # else:
                reason["error"]= "账号或密码错误，请重新输入"
                return HttpResponse(json.dumps(reason), content_type="application/json")
        else:
            reason["error"] = "账号密码不能为空"
            return HttpResponse(json.dumps(reason), content_type="application/json")
    else:
        # login_form = loginForm()
        reason["error"] = "登录失败，请重试"
        return HttpResponse(json.dumps(reason), content_type="application/json")

#ajax同步搜索关键字查询功能
def rkSearch(request):
    name = request.GET['name']
    data = []
    keywords = CareerCourse.objects.filter(search_keywords__name__icontains=name)
    for i in keywords:
        data.append({'name': i.name,
                     'color':i.course_color})
    return HttpResponse(json.dumps(data), content_type="application/json")

def lesson(request):
    return render(request, "common/lesson.html", locals())

#点击邮箱注册
@csrf_exempt
def register_email(request):
    reason = {"error": ""}
    if request.method == "POST":
        register_email = registerEmailForm(request.POST)
        if register_email.is_valid():
            username = register_email.cleaned_data['email']
            password = register_email.cleaned_data['password']
            check = register_email.cleaned_data['check']
            try:
                if UserProfile.objects.get(username=username):
                    reason = {"error": "用户已存在"}
                    return HttpResponse(json.dumps(reason), content_type="application/json")
            except:
                try:
                    UserProfile.objects.create_user(username=username,email=username,mobile=None,password=password)
                except Exception:
                    reason = {"error": "注册失败，请重试"}
                    return HttpResponse(json.dumps(reason), content_type="application/json")
                user = authenticate(username=username, password=password)
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                login(request,user)
                reason["username"] = username
                return HttpResponse(json.dumps(reason), content_type="application/json")
        else:
            # pdb.set_trace()
            print register_email.errors
            reason = {"error": error_message(str(register_email.errors))}
            return HttpResponse(json.dumps(reason), content_type="application/json")
    else:
        reason = {"error": "注册失败，请重试"}
        return HttpResponse(json.dumps(reason), content_type="application/json")

#点击手机注册
@csrf_exempt
def register_phone(request):
    reason = {"error": ""}
    if request.method == "POST":
        register_mobile = registerMobileForm(request.POST)
        if register_mobile.is_valid():
            username = register_mobile.cleaned_data['phone']
            phone=re.compile('^1[358]\d{9}$|^176\d{8}')
            phone_match=phone.match(username)
            if not phone_match:
                reason = {"error": "手机号码格式错误，请重试"}
                return HttpResponse(json.dumps(reason), content_type="application/json")
            password = register_mobile.cleaned_data['password']
            short = register_mobile.cleaned_data['checkPhone']
            check = register_mobile.cleaned_data['check']
            try:
                if UserProfile.objects.get(username=username):
                    reason = {"error": "用户已存在"}
                    return HttpResponse(json.dumps(reason), content_type="application/json")
            except:
                try:
                    UserProfile.objects.create_user(username=username,email=None,mobile=username,password=password)
                    print username+"1"
                except Exception:
                    reason = {"error": "注册失败，请重试"}
                    return HttpResponse(json.dumps(reason), content_type="application/json")
                # user = authenticate(username=username, password=password)
                # user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                # login(request,user)
                reason["username"] = username
                return HttpResponse(json.dumps(reason), content_type="application/json")
        else:
            # pdb.set_trace()
            print register_mobile.errors
            reason = {"error": error_message(str(register_mobile.errors))}
            return HttpResponse(json.dumps(reason), content_type="application/json")
    else:
        reason = {"error": "注册失败，请重试"}
        return HttpResponse(json.dumps(reason), content_type="application/json")

#密码找回功能
@csrf_exempt
def reg_password(request):
    reason = {"error": ""}
    if request.method == "POST":
        print "123"
        reg_pass = RgForm(request.POST)
        if reg_pass.is_valid():
            username = reg_pass.cleaned_data['reg']
            phone = re.compile('^1[358]\d{9}$|^176\d{8}')
            email = re.compile("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$")
            phone_match = phone.match(username)
            email_match = email.match(username)
            if not phone_match and not email_match:
                reason = {"error": "格式错误，请重试"}
                return HttpResponse(json.dumps(reason), content_type="application/json")
            try:
                if not UserProfile.objects.get(username=username):
                    reason = {"error": "用户不存在"}
                    return HttpResponse(json.dumps(reason), content_type="application/json")
                else:
                    reason["username"] = username
                    return HttpResponse(json.dumps(reason), content_type="application/json")
            except:
                reason = {"error": "用户不存在"}
                return HttpResponse(json.dumps(reason), content_type="application/json")
        else:
            # pdb.set_trace()
            reason = {"error": error_message(str(reg_pass.errors))}
            return HttpResponse(json.dumps(reason), content_type="application/json")
    else:
        reason = {"error": "输入失败，请重试"}
        return HttpResponse(json.dumps(reason), content_type="application/json")



