# encoding:utf-8

settings =[
    {
        "action": '/login',
        "method": "post",
        "integral": 10
    },
]

class IntegralMiddleware(object):
    '''积分处理中间件'''
    def process_response(self, request):
        '''api响应完后，处理积分业务'''
        pass
