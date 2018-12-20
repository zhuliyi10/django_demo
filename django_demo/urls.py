"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from hello import views as hello_view

urlpatterns = [
    path('admin/', admin.site.urls),


    url(r'^index/$',hello_view.index),#Django 1.8.x - Django 2.0 版本
    # path('index/',hello_view.index)#Django 2.0 版本

    url(r'^add/$',hello_view.add,name='add'),#采用 /add/?a=4&b=5 这样GET方法进行
    url(r'^add/(\d+)/(\d+)/$',hello_view.add2),#跳转到新的地址
    url(r'^new_add/(\d+)/(\d+)/$',hello_view.add2,name='add2'),#采用 /add/3/4/ 这样的网址的方式
    url(r'^data/$',hello_view.show_data,name='data')

]
