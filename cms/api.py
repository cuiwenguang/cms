from django.conf.urls import include, url
from tastypie.api import Api

from cms.member.resources.auth import AuthResource
from cms.member.resources.user import UserResource

v1_api = Api(api_name=u'v1')

v1_api.register(AuthResource())
v1_api.register(UserResource())

urlpatterns = [
    url(r'', include(v1_api.urls)),
]
