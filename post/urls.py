#coding=utf-8

from django.conf.urls import url
from django.urls import path
import post.views as views

urlpatterns = [
    url(r'^$', views.queryAll),
    url(r'^page/(\d+)$', views.queryAll),
    url(r'^detail/(\d+)$', views.detail),
    url(r'^category/(\d+)$', views.queryPostByCid),
    url(r'^archive/(\d+)/(\d+)$', views.queryPostByCreated)
]
