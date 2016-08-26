# encoding:utf-8

from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash

from cms.article.models import Channel,Subscribe

class ChannelResource(ModelResource):
    '''
        添加，修改，删除，获取频道(单个，列表)
        更新、获取用户订阅
    '''
    class Meta:
        queryset = Channel.objects.all()
        resource_name = 'channel'
        serializer = Serializer(formats=['json'])

    def prepend_urls(self):
        return [
            # 某一个用户订阅的频道
            url(r"^(?P<resource_name>%s)/(?p<userid>\d+)%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('subscribe'), name="subscribe"),
        ]

    def subscribe(self, request, *args, **kwargs):
        '''post:更新用户订阅；get:获取用户订阅'''
        pass

