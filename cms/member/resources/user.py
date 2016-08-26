# encoding:utf-8
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash
from cms.member.models import Friend

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['post', 'get']
        resource_name = 'member'
        serializer = Serializer(formats=['json'])

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/register%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('register'), name='api_register'),
            url(r"^(?P<resource_name>%s)/avatar%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('update_avatar'), name="update_avatar"),
            url(r"^(?P<resource_name>%s)/password%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('update_password'), name="update_password"),
            url(r"^(?P<resource_name>%s)/paypal/bind%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('bind_paypal'), name="bind_paypal"),
            url(r"^(?P<resource_name>%s)/paypal/update%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('update_paypal'), name="update_paypal"),
        ]

    def register(self, request, **kwargs):
        return HttpResponse("Hello")

    def post_detail(self, request, **kwargs):
        '''修改个人信息'''
        pass

    def update_avatar(self, request, ** kwargs):
        '''修改头像'''
        pass

    def update_password(self,request, ** kwargs):
        '''修改密码'''
        pass

    def bind_paypal(self, request, **kwargs):
        '''绑定网银'''
        pass

    def update_paypal(self, request,  **kwargs):
        '''修改网银密码'''
        pass

    def set_language(self,request, **kwargs):
        pass


class FriendResource(ModelResource):
    class Meta:
        queryset = Friend.objects.all()
        allowed_methods = ['post', 'get']
        resource_name = 'member'
        serializer = Serializer(formats=['json'])
