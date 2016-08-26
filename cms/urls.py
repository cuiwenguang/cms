from django.conf.urls import include, url
from django.contrib import admin
from oauth2_provider import urls as oauth_urls
from cms.member import urls as member_api
from cms.member.api import test2
from cms.member.views import ApiEndpoint
import api
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/oauth2/', include(oauth_urls, namespace='oauth2_provider')),
    url(r'^test/$', ApiEndpoint.as_view()),
    url(r'^test2/$', test2),
    url(r'^api/', include(api)),
]
