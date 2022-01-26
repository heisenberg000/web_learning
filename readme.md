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