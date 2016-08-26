# encoding:utf-8

from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash

from cms.article.models import Article


class FavoriteResource(ModelResource):
    '''
        添加，修改，删除，获取频道(单个，列表)
        更新、获取用户订阅
    '''

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'favorite'
        serializer = Serializer(formats=['json'])
