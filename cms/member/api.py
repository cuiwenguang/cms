# encoding:utf-8
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.views.base import TokenView
from requests.auth import HTTPBasicAuth
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from django.shortcuts import HttpResponse
import json
import requests

from cms.utils.http import StatusCode, create_json_resposne

def test2(request):

    url = 'http://127.0.0.1:8000/api/oauth2/token/'

    token_request_data = {
        'grant_type': 'password',
        'username': 'admin',
        'password': 'by123456',
    }
    client_id = 'VpL2mTHlynQdHbHNFbjH2ajFuvSBGZ7pTXbfLaB0'
    client_secret = '3zxGWfe0OFkFIA8wm3cx12ix9Btcv4jVdZabCCsZmEQaB3N8hGg2JiD5Vw6jue3HZl5mpZ46hLm7aFtBV5J1wxyl5TJGM4nir76Lr8YH6Los2KoaNyImO2v40ixcWJGW'

    auth_header = HTTPBasicAuth(client_id, client_secret)
    res = requests.post(url,  data=token_request_data, auth=auth_header)
    return HttpResponse(res.text)



class LoginView(TokenView):
    def post(self, request, *args, **kwargs):
        res = super(LoginView, self).post(request, *args, **kwargs)
        oauth_data = json.loads(res.content)
        return create_json_resposne(request, data=oauth_data)


@csrf_exempt
def user_info(request, token):
    id = AccessToken.objects.get(token=token).user_id
    user = User.objects.get(pk=id)
    return create_json_resposne(request,data=user)

@csrf_exempt

def register(request):
    '''注册'''
    from cms.utils.validators import validate_email
    req_data= json.loads(request.body)

    if User.objects.filter(username=req_data['username']):
        return create_json_resposne(request, status_code=StatusCode.VALIDATE_ERROR,
                                    message='username is existed')

    if req_data['password'] != req_data['confirm_pwd']:
        return create_json_resposne(request, status_code=StatusCode.VALIDATE_ERROR,
                                    message = 'passswords does not match')

    if  not validate_email(req_data['email']) and len(req_data['email']):
        return create_json_resposne(request, status_code=StatusCode.VALIDATE_ERROR,
                                    message = 'Email format error')

    user = User.objects.create_superuser(req_data['username'],
                                         req_data['email'],
                                         req_data['password'])
    user.is_superuser=False
    user.is_active = req_data["is_temp"]
    user.save()

    res_data = {
        'id': user.id
    }
    return create_json_resposne(request, data=res_data)



def update_Info(request):
    '''修改个人信息'''
    pass

def update_password(request):
    '''修改密码'''
    pass

def bind_paypal(request):
    '''绑定网银'''
    pass

def update_pay_password(request):
    '''修改提现密码'''
    pass

def my_Favorites(request):
    '''我的收藏'''
    pass

def my_comments(request):
    '''我的评论'''
    pass

def my_subscribe_channels(request):
    '''我订阅的频道'''
    pass