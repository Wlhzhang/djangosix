from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class MyAuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 获取请求
        no_auth_path = ['/','/login/','/polls/register/','/polls/get_code/','/polls/login/']
        if (request.path in no_auth_path)==False:
            if (request.user.is_authenticated and request.user.is_active and request.user.is_staff)==False:
                print('未登录')
                return redirect('/')

    # 响应数据
    def process_response(self,request,response):
        return response

    # 异常处理
    def process_exception(self,request,exception):
        print('exception')