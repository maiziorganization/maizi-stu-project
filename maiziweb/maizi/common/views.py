#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render,redirect,HttpResponse
from models import Ad,Course,RecommendKeywords,CareerCourse
from django.conf import settings
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

# 首页
def index(request):
    ad_list = Ad.objects.all()
    course_list = Course.objects.all()
    return render(request, "common/index.html", locals())

def rkSearch(request):
    name = request.GET['name']
    print name
    print "11"
    data = []
    keywords = CareerCourse.objects.filter(search_keywords__name__icontains=name)
    print keywords
    for i in keywords:
        print i.name
        print i.course_color
        data.append({'name': i.name,
                     'color':i.course_color})
    return HttpResponse(json.dumps(data), content_type="application/json")




