#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render,redirect,HttpResponse
from models import Ad,Course,RecommendKeywords,CareerCourse,UserProfile
from django.conf import settings
from form import *
from django.contrib.auth import logout, login, authenticate
from django.core.serializers import serialize
import json

import logging

logger = logging.getLogger('maizi.common.views')

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
    # # 分类信息获取（导航数据）
    # category_list = Category.objects.all()[:6]
    # # 文章归档数据
    # archive_list = Article.objects.distinct_date()
    # # 广告数据
    # ad_list = Advert.objects.all()[:4]
    # # 标签云数据
    # tag_list = Tag.objects.all()
    # # 友情链接数据
    # link_list = Links.objects.all()
    # # 浏览排行榜数据
    # archive_list_top = Article.objects.all().order_by('-click_count')
    # # 评论排行
    # #定义一个变量comment_count来计数article的数量
    # #相当于select count(*) from Comment c group by c.article order by count(*)
    # comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    # article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    # #站长推荐
    # admin_recommend_list = Article.objects.all().order_by('-score')
    return locals()

#
def index(request):
    ad_list = Ad.objects.all()
    course_list = Course.objects.all()
    return render(request, "common/index.html", locals())
#点击登入
#首页
def my_login(request):
    ad_list = Ad.objects.all()
    course_list = Course.objects.all()
    reason = {"error": ""}
    if request.method == "POST":
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                login(request,user)
                reason["username"] = username
                return HttpResponse(json.dumps(reason), content_type="application/json")
            else:
                reason["error"]= "账号或密码错误，请重新输入"
                return HttpResponse(json.dumps(reason), content_type="application/json")
        else:
            print "1"
            reason["error"] = "账号密码不能为空"
            return HttpResponse(json.dumps(reason), content_type="application/json")
    else:
        login_form = loginForm()
        return render(request,"common/index.html", locals())

#ajax同步搜索关键字查询功能
def rkSearch(request):
    name = request.GET['name']
    data = []
    keywords = CareerCourse.objects.filter(search_keywords__name__icontains=name)
    for i in keywords:
        data.append({'name': i.name,
                     'color':i.course_color})
    return HttpResponse(json.dumps(data), content_type="application/json")



#点击邮箱注册
def register_email(request):
    pass

#点击手机注册
def register_phone(request):
    pass




