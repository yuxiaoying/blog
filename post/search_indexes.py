#coding=UTF-8
from haystack import indexes
from post.models import *

#注意格式（模型类名+Index）
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    #页面中的
    text = indexes.CharField(document=True, use_template=True)
    #给title,content设置索引 对应模型类的属性名
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')
    # 重写： 返回搜索的模型类
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')