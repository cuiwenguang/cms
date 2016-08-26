# encoding:utf-8
from django.db import models
from django.utils import timezone
# Create your models here.


class Channel(models.Model):
    channel_name = models.CharField(max_length=20)  # 频道名称
    channel_group = models.CharField(max_length=20) # 频道板块，news,knowledge
    channel_status = models.IntegerField(default=1) # 1：可用；0：不可用
    parent_id = models.IntegerField(default=0) #备用字段，满足频道分类树形结构需要
    language = models.CharField(max_length=20,  default='en')
    cover_img = models.CharField(max_length=255)
    order_index = models.IntegerField(default=0) # 排序序列

class Article(models.Model):
    '''
        文章信息表
    '''
    title = models.CharField(max_length=255) # 标题
    create_date = models.DateTimeField(default=timezone.now) # 日期
    channel_id = models.IntegerField() # 所属频道
    cover = models.CharField(max_length=500) # 列表封面图片，多张一逗号分隔
    template = models.IntegerField() # 列表显示风格模板：一张小图，一张大图，三联图
    content = models.TextField() # 文章内容，如果是原创投稿，保存文章内容，如果是转载，只保存摘要
    is_original = models.BooleanField(default=False) # 是否原创
    source = models.CharField(max_length=50) # 如转载，保存文章来源
    user_id = models.IntegerField(default=0) # 如原创投稿，保存投稿人ID,0表示系统转载
    user_name = models.CharField(max_length=50,null=True,blank=True) # 冗余字段，保存投稿人姓名
    user_avatar = models.CharField(max_length=255) # 冗余，用户头像
    status = models.IntegerField(default=0) #文章状态 0：草稿；1：发布；-1：删除
    comment_num = models.IntegerField(default=0) # 评论数
    agree_num = models.IntegerField(default=0) # 点赞数
    page_url = models.CharField(max_length=500) # 原文链接
    update_date = models.DateTimeField(null=True, blank=True)
    language = models.CharField(max_length=20, default='en')
    category = models.CharField(max_length=20, null=True,blank=True) # 板块分类，方便查询


class Comment(models.Model):
    '''评论'''
    comment_content = models.CharField(max_length=255)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_avatar = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    agree_num = models.IntegerField(default=0)  # 点赞数


class Tag(models.Model):
    article_id = models.IntegerField()
    tag_words = models.CharField(max_length=50)
    language = models.CharField(max_length=20, default='en')


class ArticleLog(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_avatar = models.CharField(max_length=255)
    article_id = models.IntegerField()


class CommentLog(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50)
    user_avatar = models.CharField(max_length=255)
    comment_id = models.IntegerField()

class Favorite(models.Model):
    '''收藏'''
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    article_id = models.IntegerField()
    collect_date = models.DateTimeField(default=timezone.now)

class Subscribe(models.Model):
    '''我订阅的频道'''
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    channel_id = models.IntegerField()
    channel_name = models.CharField(max_length=50)


