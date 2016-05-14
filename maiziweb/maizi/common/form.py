#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015/10/27
@author: yopoing
Model管理，包含各个模块所需要的数据模型，由项目组长统一管理。
'''

from django import forms
from models import UserProfile

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control','placeholder':'请输入邮箱账号/手机号','id':'username_id'}),max_length=50)
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'请输入密码','id':'password_id'}))

class registerEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'请输入邮箱账号'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'请输入密码'}))
    check = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'请输入验证码'}))

class registerMobileForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'请输入手机号'}))
    checkPhone = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'请输入短信验证码'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'请输入密码'}))
    check = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'请输入验证码'}))
