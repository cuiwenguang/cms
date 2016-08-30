# encoding:utf-8
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash
from tastypie.http import HttpUnauthorized

from cms.utils.gust import generate_gust_account


class AuthResource(ModelResource):
    '''
        用户认证：注册，登录，注销
    '''
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['post', 'get']
        resource_name = 'auth'
        serializer = Serializer(formats=['json'])


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
        ]

    def login(self, request, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        is_new_gust = request.POST.get('is_gust', False)

        if is_new_gust:
            user = self._create_gust()

        user = authenticate(username=username,password=password)

        if user==None:
            return self.create_response(request,
                                        data={
                                            "error":"错误得用户名或密码"
                                        },
                                        response_class=HttpUnauthorized)

        login(request, user)

        return self.create_response(request,
                                    data={
                                        "id": user.id,
                                        "name": user.username

                                    })
    def logout(self, request, **kwargs):
        logout(request)
        return self.create_response(request, data='')


    def _create_gust(self):
        username = generate_gust_account(randomlength=10)
        user = User.objects.create(username, email='', password='')
        return user

