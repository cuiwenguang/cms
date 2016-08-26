# encoding:utf-8

from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash

from cms.article.models import Comment, CommentLog

class CommentResource(ModelResource):
    '''
        添加，修改，删除，获取频道(单个，列表)
        更新、获取用户订阅
    '''
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        serializer = Serializer(formats=['json'])

    def prepend_urls(self):
        return [
            # 某一个用户订阅的频道
            url(r"^(?P<resource_name>%s)/vote%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('vote'), name="article_vote"),
        ]

    def vote(self, request, **kwargs):
        pass


class CommentLogResource(ModelResource):
    '''
        添加，修改，删除，获取频道(单个，列表)
        更新、获取用户订阅
    '''
    class Meta:
        queryset = CommentLog.objects.all()
        resource_name = 'commentlog'
        serializer = Serializer(formats=['json'])
