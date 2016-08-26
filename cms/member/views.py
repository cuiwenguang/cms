from django.shortcuts import HttpResponse,render
from oauth2_provider.views.generic import ProtectedResourceView
import requests

# Create your views here.
def oauth_test(request):
    data = {
        u'WV_deNEbpVxn@6u7zRwy70_W@-?lHrskp2S.2bxA': u'P;AjBjD76tL;UI3:IXCy3ha0OmB1sesNoYQ?!tGKX70d@vcTuNwseuIl@=h1NTH_uEpQbO3_NFgXrw9dbUdMmvX_qkDd5POHQ7VjvnAMY20UpkiX2-Y3N.Ju?;1ogJ7B',
        'grant_type': 'password',
        'username': 'admin',
        'password': '123',
    }
    res = requests.post('http://localhost:8000/oauth/token/', data=data)
    # res = requests.post('http://localhost:8000/loginCallBack/', data=data)
    return HttpResponse(res.text)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello Oauth2')


