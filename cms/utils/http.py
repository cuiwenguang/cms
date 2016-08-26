from django.http import JsonResponse
from django.db import models
from django.forms.models import  model_to_dict

class StatusCode:
    SUCESS = 200
    VALIDATE_ERROR = 450


def create_json_resposne(request,
                         status_code=StatusCode.SUCESS,
                         message='', data=None):

    if isinstance(data,models.Model):
        ret = model_to_dict(data)
    else:
        ret = data

    result = {
        'state': status_code,
        'message': message,
        'data': ret
    }

    return JsonResponse(result)


def request_methods(view):
    def decorator(request, *args, **kwargs):
        pass
    def fail_handler(request):
        pass