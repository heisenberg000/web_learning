from email import header


# -*- encoding: utf-8 -*-
'''
@File    :   testdb.py
@Time    :   2022/01/26 23:41:29
@Author  :   James 
@Version :   1.0
@Desc    :   测试db
'''

from django.http import HttpResponse

from test_model.models import Test

def testdb(request):
    t = Test(name="测试Django DB")
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def getTestData(request):
    # 获取所有数据
    list = Test.objects.all()
    # where筛选
    # res = Test.objects.filter(id=1)
    # 获取单个对象
    # single  = Test.objects.get(id=1)
    # 限制返回数据
    # Test.objects.order_by("name")[0:2]
    # 数据排序
    # Test.objects.filter(name="测试Django DB").order_by("id")

    for v in list:
        r = v.name + " "
    
    return HttpResponse("<p>" + r +"</p>")

def updateTestData(request):
    # test = Test.objects.get(id=1)
    # test.name = "测试Django 用户修改"
    # test.save()
    Test.objects.filter(id=1).update(name="测试Django 用户修改")
    return HttpResponse("<p>数据修改成功</p>")

def delTestData(request):
    # test = Test.objects.get(id=1)
    # test.delete()
    Test.objects.filter(id=1).delete()
    return HttpResponse("<p>数据删除成功</p>")
