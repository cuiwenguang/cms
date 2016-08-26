# encoding:utf-8
from abc import ABCMeta, abstractmethod
from django.core.urlresolvers import  reverse
from django.shortcuts import redirect
import cms.settings


class AuthBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = ''
        self.app_id = ''
        self.app_type = ''
        self.app_secret = ''
        self.auth_grant = ''
        self.callback = ''

    @abstractmethod
    def login(self, request, **kwargs):pass

class Auth_local(AuthBase):
    '''本地登录，通过本地oauth2授权'''
    def __init__(self):
        self.app_id = cms.settings.APP_ID
        self.app_secret = cms.settings.APP_SECRET
        self.auth_grant = 'password'

    def login(self, request, **kwargs):
        res = redirect(reverse('token'))

class Auth_facebook(AuthBase):
    '''
    第三方登录，首先通过第三方的oauth授权.
    通过openid获取到用户信息以后,保存在本地
    然后调用本地的oauth授权，即最终的客户端授权令牌还是本地发的，第三方只是登录获取一些用户信息缓存本地,和本地账户进行绑定
    '''
    def __init__(self):
        pass

    def login(self, request, **kwargs):
        pass


class Factory:
    def create_auth(self, mode='local'):
        auth = getattr(self.__module__, "Auth_%s" % mode.lower(), "")
        if auth == "":
            return Auth_local

        return auth
