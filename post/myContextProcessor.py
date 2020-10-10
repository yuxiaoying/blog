#coding=utf-8
from django.db.models import Count
from post.models import Post

def getRightInfo(request):
    #获取分类信息
    r_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')
    #获取近期文章
    r_recPost = Post.objects.all().order_by('-created')[:3]
    #获取日期归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select created ,COUNT(*) c from t_post group by DATE_FORMAT(created,'%Y-%m') order by c desc,created desc")
    r_filepost = cursor.fetchall()

    return {'r_catepost': r_catepost, 'r_recPost': r_recPost, 'r_filepost':r_filepost}
