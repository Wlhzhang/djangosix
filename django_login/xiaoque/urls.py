from django.urls import path,re_path

from xiaoque.views import get_xiaoque, addxiaoque, dis_xiaoque

urlpatterns=[
    # re_path('get_register/$',get_register,name='get_register'),
    re_path(r'^get_xiaoque/$', get_xiaoque, name='get_xiaoque'),
    re_path(r'^addxiaoque/$', addxiaoque, name='addxiaoque'),
    re_path('dis_xiaoque/$', dis_xiaoque, name='dis_xiaoque')
]
