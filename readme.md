## Django 学习笔记

1. ### 自定义配置
- 新建templatetags目录
- 在settings中配置libraries
- register名称不可更改

2. ### 静态资源目录
- 新建statics目录
- 在settings中配置STATICFILES_DIRS

3. ### 连接数据库
- 安装mysql驱动：pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
- 新建app：django-admin startapp [app名称]
- 在settings中配置DATABASES和INSTALLED_APPS
- 自动创建表结构
    - python manage.py makemigrations [app名称]
    - python manage.py migrate [app名称]

4. ### Request对象及方法
#### 对象：
- path 输出请求路径，不包括域名
- method GET/POST
- GET 一个QueryDict对象
- POST 一个QueryDict对象
- REQUEST GET和POST属性的结合体
- COOKIES 标准Python字典对象
- FILES 字典对象（请求为POST，且form中含有enctype="multipart/form-data"属性
    - key `<input type="file" name="file1">`中name
    - value 字典对象
        - filename 文件名
        - content-type
        - content (一般base64)
- META HTTP头部信息字典
- user 当前登录用户，`django.contrib.auth.models.User`对象
- session 唯一可读写属性。会话字典对象
- raw_post_data 原始HTTP POST数据
- body 请求体，如二进制图片、XML、Json
#### 方法：
- `__getitem__(key)` 返回POST/GET属性键值，先取POST，再取GET
- `has_key(key)` POST和GET属性中是否包含key
- `get_full_path()` 返回包含查询字符串的请求路径
- `is_secure()` 请求是否安全，True说明是HTTPS发送的请求

5. ### QueryDict对象
- `__getitem__` key对象多个value时，返回最后一个value
- `__setitem__` 设置key和value列表
- `get()` 同getitem方法
- `update()` 向字典中的key添加items，不是替换
- `items()` 返回单值key - value
- `values()` 返回单值key
- `getlist(key) / setlist(key,list)` 返回/设置key对应的value列表
- `appendlist(key,list)` 添加item到key关联的内部list
- `lists()` 返回key对应的值列表(list)
- `urlencode()` 返回一个以查询字符串格式进行格式化后的字符串(例如："a=2&b=3&b=5")

6. ### 视图
- request 请求对象
- HttpResponse 响应对象
- render 跳转到某个页面
- redirect 重定向

7. ### 路由
- 一般路由
- 正则路由/正则命名路由 如 `^index/$ ^(?P<分组名>\w+)`
- 路由分发 `include('app01.urls')`
- 反向解析路由 通过name解析
    - 模板 templates 中的 HTML 文件中，利用 `{% url "路由别名" %}` 反向解析
    - 视图 views 中，`return redirect(reverse(路由别名))`
    - 命名空间 `include(("app名称：urls","app名称"))` `reverse("app名称：路由别名")`
8. ### Admin 管理工具
