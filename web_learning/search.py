# -*- encoding: utf-8 -*-
'''
@File    :   search.py
@Time    :   2022/01/27 15:42:03
@Author  :   James 
@Desc    :   search.py
@Version :   1.0
'''

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

def search_form(request):
    return render(request,"search_form.html")

def search(request):
    request.encoding = "utf-8"
    print(request.GET)
    if "q" in request.GET and request.GET["q"]:
        message = "搜索内容：{}".format(request.GET["q"])
    else:
        message = "你提交了空表单"
    return HttpResponse(message)

def search_post(request):
    ctx = {}
    if request.POST:
        ctx["rlt"] = request.POST["q"]
    return render(request,"search_form.html",ctx)