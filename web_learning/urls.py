"""web_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from . import views,testdb,search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.demo),
    path('child/',views.child),
    path('testdb/',testdb.testdb),
    path('getData/',testdb.getTestData),
    path('updateData/',testdb.updateTestData),
    path('delData/',testdb.delTestData),
    url(r'^search-form/$',search.search_form),
    path('search/',search.search),
    path('search-post/',search.search_post),
    url(r'^process/$',views.processBody),
    url(r'^user/(?P<id>\d{2})/$',views.user),  # 一个分组代表一个形参,?P<形参名>
    re_path(r'^index/$',views.index,name='index'),
    re_path(r'^login/(\d{2})/$',views.jlogin,name='jlogin')
]
