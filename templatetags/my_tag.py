# -*- encoding: utf-8 -*-
'''
@File    :   my_tag.py
@Time    :   2022/01/26 22:54:22
@Author  :   James 
@Version :   1.0
@Desc    :   自定义标签和过滤器
'''

from django import template

register = template.Library() # register是固定的，不可改变

@register.filter
def my_filter(v1,v2):
    return v1 * v2

@register.simple_tag
def my_tag(v1,v2,v3):
    return v1 * v2 * v3