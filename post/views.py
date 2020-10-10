from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
# 渲染主页面
from post.models import *

from django.views.decorators.cache import cache_page

@cache_page(60*15)
def queryAll(request, num=1):
    #第几页
    # n = int(request.GET.get('num', 1))
    # print(n)
    n = int(num)
    #获取所有帖子
    postList = Post.objects.all().order_by('-created')
    #每页显示记录
    pageSize = 1
    #创建分页器对象
    pageObj = Paginator(postList, pageSize)
    #获取当前页的数据
    try:
        perpage = pageObj.page(n)
    except PageNotAnInteger:
        perpage = pageObj.page(1)
    except EmptyPage:
        perpage = pageObj.page(1)
    if n <= 5:
        if pageObj.num_pages <= 10:
            pagenumlist = range(1, pageObj.num_pages+1)
        else:
            pagenumlist = range(1, 11)
    if n > 5:
        if (n + 5 < pageObj.num_pages):
            pagenumlist = range(n - 5, n + 5)
        else:
            pagenumlist = range(pageObj.num_pages - 9, pageObj.num_pages + 1)
    from django.db import connection
    print(connection.queries[-1]['sql'])
    return render(request, 'index.html', {'postList': perpage, 'pagenumlist': pagenumlist, 'currentpagenum': n})


def detail(request, postid):
    postid = int(postid)
    #根据postid查询帖子的详细信息
    post = Post.objects.get(id=postid)
    return render(request, 'detail.html', {'post': post})


def queryPostByCid(request, cid):
    postList = Post.objects.filter(category_id=cid)
    return render(request, 'article.html', {'postList': postList})


def queryPostByCreated(request, year, month):
    postList = Post.objects.filter(created__year=year, created__month=month)
    return render(request, 'article.html', {'postList': postList})