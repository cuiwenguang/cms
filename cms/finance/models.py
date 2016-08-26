# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Withdrawals(models.Model):
    '''提现'''
    user = models.ForeignKey(User)
    apply_date = models.DateTimeField(default=timezone.now) # 申请日期
    amount = models.IntegerField() # 申请兑换金额
    audit = models.IntegerField() # 审核状态：1提交申请；2：通过审核并转账；3提现完成


class IntegralDetail(models.Model):
    '''积分明细'''
    action = {'read': 1, 'vote': 3, 'comment': 5, 'login':5, 'register': 20}

    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    integral_action = models.CharField(max_length=10) # 获取积分的行为 action
    integral_num = models.IntegerField() # 获取的积分数