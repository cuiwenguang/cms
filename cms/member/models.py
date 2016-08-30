# encoding:utf-8
from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

from cms.utils.image import upload_image


# Create your models here.
class Profile(models.Model):
    '''会员扩展信息'''
    user = models.OneToOneField(User)
    pya_pwd = models.CharField(max_length=50)  # 支付提现密码
    location = models.CharField(max_length=50, null=True, blank=True) # 所在地
    avatar = models.CharField(max_length=255) # 头像
    job = models.CharField(max_length=50, null=True, blank=True) # 工作
    mobile = models.CharField(max_length=20, null=True, blank=True) # 电话
    mobile_code = models.CharField(max_length=100,  null=True, blank=True) # 手机编码
    integral = models.IntegerField(default=0) # 资产（积分）
    paypal = models.CharField(max_length=50) # 网银账号
    language = models.CharField(max_length=20, default='en') # 语言

    def bind_mobile(self, mobile, validate_code=''):
        '''
        绑定手机
        :param validate_code:手机验证码
        :return:
        '''
        self.mobile = mobile
        self.save()

    def bind_paypal(self, paypal, pwd, validate_code):
        '''
        绑定网银
        :param paypal:网银账号
        :param pwd: 支付密码
        :param validate_code: 验证码
        :return:
        '''
        self.paypal = paypal
        self.pya_pwd = pwd
        self.save()

    def update_integral(self, num):
        self.integral += num
        self.save()

    def set_avatar(self, x, y, w, h):
        self.avatar = upload_image(None,x,y,w,h)
        self.save()

    def set_profile(self, **kwargs):
        self.location=kwargs['location']
        self.job = kwargs['job']
        self.language = kwargs['language']
        self.save()


class Oauth2(models.Model):
    '''第三方授权信息'''
    user = models.ForeignKey(User)
    oauth_name = models.CharField(max_length=20)
    open_id = models.CharField(max_length=50)

class Friend(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    follow_id = models.IntegerField(null=True, blank=True)