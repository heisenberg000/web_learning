# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2022/01/26 22:34:27
@Author  :   James 
@Version :   1.0
@Desc    :   视图py
'''

from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime 
from django.urls import reverse
import json

def demo(request):
    v_dict = {}
    v_dict["t_var"] = "这是一个变量"
    v_dict["t_name"] = "aLBeRt eiNStEin"
    v_dict["t_none"] = []
    v_dict["t_date"] = datetime.now()
    v_dict["t_script"] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    v_dict["t_list"] = ["姓名"]
    v_dict["t_std_list"] = ["小明","小红","小王","小张","小赵"]
    v_dict["t_dict"] = {
        "篮球运动员": ["姚明","科比","詹姆斯"],
        "足球运动员": ["C罗","梅西","李铁"]
    }
    return render(request,"demo.html",v_dict)

def child(request):
    return render(request,"child.html")

def processBody(request):
    print("path属性:",request.path)
    print("method属性：",request.method)
    print("COOKIES属性：",request.COOKIES)
    print("META属性：",request.META)
    print("session属性：",request.session)
    print("fullpath:",request.get_full_path())
    # print("raw_post_data属性：",request.raw_post_data)
    json_str = request.body
    print(json.loads( json_str.decode("utf-8")))
    return HttpResponse("ok")

def user(request,id):
    m = request.method
    print("user_id:",id)
    return HttpResponse("ok")

def index(request):
    return render(request,"login.html")

def jlogin(request,age):
    if request.method == "GET":
        return HttpResponse("OK")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "django" and password == "django":
            return render(request,"demo.html")
        else:
            return redirect(reverse("index"))