# encoding:utf-8
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash
import tastypie.http
import json

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
                self.wrap_view('set_avatar'), name="set_avatar"),
            url(r"^(?P<resource_name>%s)/password%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('update_password'), name="update_password"),
            url(r"^(?P<resource_name>%s)/paypal/bind%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('bind_paypal'), name="bind_paypal"),
            url(r"^(?P<resource_name>%s)/mobile%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('bind_mobile'), name="bind_mobile"),
        ]

    def register(self, request, **kwargs):
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        email = json_data['email']

        if User.objects.filter(username=username).exists():
            return self.create_response(request,data={'error': '用户名已存在'},
                                        response_class=tastypie.http.HttpForbidden)

        user = User.objects.create_user(username,email=email,password=password)

        return self.create_response(request,
                                    data={
                                         "id": user.id,
                                         "username":user.username
                                    })

    def set_avatar(self, request, ** kwargs):
        '''修改头像'''
        profile = request.user.get_profile()
        image = request.FILES
        x = request.POST.get('x', 0)
        y = request.POST.get('y', 0)
        w = request.POST.get('w', 50)
        h = request.POST.get('h', 50)
        try:
            profile.set_avatar(image,x,y,w,h)
        except:
            self.create_response(request,data={'error':'服务器发生错误，上传文件失败'},
                                 response_class=tastypie.http.HttpApplicationError)

    def update_password(self,request, ** kwargs):
        json_data = json.loads(request.body)
        old_pwd = json_data['old_pwd']
        new_pwd = json_data['new_pwd']
        user = authenticate(username=request.user.username, password=old_pwd)

        if user == None:
            return self.create_response(request,data={'error': '原密码错误'},
                                        response_class=tastypie.http.HttpForbidden)

        user.set_password(new_pwd)
        return self.create_response(request, data={})


    def bind_paypal(self, request, **kwargs):
        profile = request.user.get_profile()
        json_data=json.loads(request.body)
        profile.bind_paypal(json_data['paypal'],json_data['pwd'],json_data['validate_code'])

        return self.create_response(request,data={'info':'绑定成功'})


    def update_integral(self, request,  **kwargs):
        '''修改网银密码'''
        profile = request.user.get_profile()
        profile.update_integral(5)

        return self.create_response(request,data={'info':'积分已修改'})

    def set_profile(self, request, **kwargs):
        profile = request.user.get_profile()
        json_data = json.loads(request.body)

        profile.set_profile(
            language=json_data['language'],
            location=json_data['location'],
            job=json_data['job']
        )

        return self.create_response(request,data={'info':'个人资料已更新'})

    def bind_mobile(self, request, **kwargs):
        json_data = json.loads(request.body)
        profile = request.user.get_profile()
        profile.bind_mobile(json_data['mobile'], json_data['validate_code'])

        return self.create_response(request,data={'info':'手机绑定成功'})


class FriendResource(ModelResource):
    class Meta:
        queryset = Friend.objects.all()
        allowed_methods = ['post', 'get']
        resource_name = 'member'
        serializer = Serializer(formats=['json'])
