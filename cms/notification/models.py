# encoding:utf-8
from django.db import models

# Create your models here.

class Notification(models.Model):
    '''
        系统消息，通知
        如果是广播，发给所有人，不保存数据库，本次不做，后面通过消息队列完成，本模块只正对特定一些用户的通知，
        如：用户安装完成后，系统发送消息，告知注册登录看新闻送积分，积分累计到一定数量后，系统发通知告知可以提现等等。
    '''
    from_user =models.CharField(max_length=50) # 发送人，一般是是消息创建人，目前不做聊天，创建人为后台管理人员
    to_user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=10)
    content = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)