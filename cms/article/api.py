# encoding:utf-8
from django.shortcuts import HttpResponse, render

def channels(request):
    '''频道'''
    pass

def article_list(request):
    '''文章列表'''
    pass

def get_artiles_by_channel(request):
    '''某一频道文章列表'''
    pass

def article_detail(request):
    '''获取一篇文章（mongodb）'''
    pass

def vote_article(request):
    '''点赞一篇文章'''
    pass

def comment_article(request):
    '''评论一篇文章'''
    pass

def collect_article(request):
    '''收藏文章'''
    pass

def share_article(request):
    '''
        文章分享
        分享文章一般服务端不做处理，但如果风向送积分，则需要实现一定逻辑
    '''
    pass

def vote_comment(request):
    '''点赞评论'''
    pass