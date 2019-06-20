import os

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from django_login import settings
from polls.cache_img import get_cache_code_info
from polls.forms import UserForm


def register(request):
    return render(request,'register.html')

# 验证码
def get_code(request):
    img,code = get_cache_code_info()
    request.session['code'] = code
    return HttpResponse(img.getvalue(),content_type='image/png')

def handle_uploaded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,'register.html')
    def post(self,request,*args,**kwargs):
        # 必须把request.files传递到form的构造函数中
        form = UserForm(request.POST,request.FILES)
        password1 = form.cleaned_data['userPassword1']
        password2 = form.cleaned_data['userPassword2']
        if password1==password2:
            if form.is_valid():
                form_file = User(
                                headimage=form.cleaned_data['my_file'],username=form.cleaned_data['userName'],
                                 password=password1,userEmail=form.cleaned_data['userEmail'])
                form_file.save()
                return render(request,'login.html')
            else:
                return JsonResponse({'status':'fail','msg':form.errors().as_json()})
        else:
            return JsonResponse({'status':'fail','msg':'密码输入不一致'})


def login(request):
    forms = UserForm(request.POST)
    code = request.POST.get('cache_code',None)
    if code == request.session['code']:
        if forms.is_valid():
            user = auth.authenticate(username=forms.cleaned_data['username'],password=forms.cleaned_data['password'])
            if user:
                auth.login(request,user)
                return JsonResponse({'msg':'登录成功','status':'success'})
            else:
                return JsonResponse({'msg':'用户名或者密码错误','status':'fail'})
        else:
            form_error = forms.errors.as_json()
            return JsonResponse({'msg':'格式不正确','data':form_error,'status':'form_error'})
    else:
        return JsonResponse({'msg':'验证码错误','status':'fail'})