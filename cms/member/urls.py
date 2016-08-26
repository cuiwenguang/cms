from django.conf.urls import include, url
from django.contrib import admin
from cms.member import api

urlpatterns = [
    url('^/register$', api.register, name='register'),
    url('^/login$',api.LoginView.as_view(), name='login'),
    url('^/(?P<token>\w{30})', api.user_info, name="user_info"),
]