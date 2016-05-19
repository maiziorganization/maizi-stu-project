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
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','class':'form-control','placeholder':'请输入密码','id':'password_id'}))

class registerEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'type': 'text', 'class': 'form-control','placeholder':'请输入邮箱账号','id':'registerEmail'}),
        error_messages={'required':'邮箱不能为空', 'invalid':'请输入正确的邮箱',},)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'type':'password','class':'form-control','placeholder':'请输入密码','id':'registerEmailPassword'}),
        error_messages={'required': '密码不能为空', 'invalid': '请输入至少8位密码','min_length': '请输入至少8位密码', 'max_length': '最多为50位密码'},
        min_length=8, max_length=50)
    check = forms.CharField(widget=forms.TextInput(
        attrs={'type':'text','class':'form-control form-control-captcha fl"','placeholder':'请输入验证码','id': 'registerEmailCheck'}),
        error_messages={'required':'验证码不能为空'})

class registerMobileForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control form-control-phone fl', 'placeholder': '请输入手机号', 'id': 'reg_mob'}),
        error_messages={'required':'手机号码不能为空'})
    checkPhone = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text','class': 'form-control','placeholder':'请输入短信验证码', 'id': 'check_phone'}),
        error_messages={'required':'请输入手机验证码'})
    password = forms.CharField(widget=forms.TextInput(
        attrs={'type':'password','class':'form-control','placeholder':'请输入密码', 'id': 'reg_password'}),
        error_messages={'required': '密码不能为空', 'invalid': '请输入至少8位密码', 'min_length': '请输入至少8位密码', 'max_length':'最多为50位密码'},
        min_length=8,max_length=50)
    check = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text','class': 'form-control form-control-captcha fl', 'placeholder': '请输入验证码', 'id': 'mbl_chk'}),
        error_messages={'required': '验证码不能为空'})
