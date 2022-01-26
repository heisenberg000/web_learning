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