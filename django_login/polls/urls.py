from django.urls import path,re_path

from polls.views import register, get_code, login, Register

urlpatterns=[
    re_path('register/$',register,name='register'),
    re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^login/$',login,name='login'),
    re_path(r'^register/$', Register.as_view(), name='register')
]
