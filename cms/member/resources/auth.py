# encoding:utf-8
from django.contrib.auth.models import User
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash
import json
from oauth2_provider.views.base import TokenView

class AuthResource(ModelResource):
    '''
        用户认证：注册，登录，注销
    '''
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['post', 'put']
        resource_name = 'auth'
        serializer = Serializer(formats=['json'])


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login_callback'), name="api_login"),
        ]

    def login_callback(self, request, **kwargs):
        '''第三方登录认证后的回调函数'''
        pass