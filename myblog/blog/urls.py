#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article/$', views.article, name='article'),
    url(r'^edit/$', views.edit, name='edit'),
    # url(r'^$', 'blog.views.index', name='add'),

]
