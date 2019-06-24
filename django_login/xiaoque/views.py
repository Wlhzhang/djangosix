from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from xiaoque.forms import TaskForm
from xiaoque.models import AddTask


def get_xiaoque(request):
    return render(request,'xiaoque.html')

# 添加消缺任务
def addxiaoque(request):
   if request.method == 'POST':
        # 必须把request.files传递到form的构造函数中
        form = TaskForm(request.POST)
        if form.is_valid():
            form_file = AddTask(
                            task_id=form.cleaned_data['task_id'],
                            task_name=form.cleaned_data['task_name'],
                            inspect_line=form.cleaned_data['inspect_line'],
                            inspect_user = form.cleaned_data['inspect_user'],
                            state = form.cleaned_data['state'],
                            pole_beg = form.cleaned_data['pole_beg'],
                            pole_end=form.cleaned_data['pole_end'],
                            df_username=form.cleaned_data['df_username'],
                            df_date=form.cleaned_data['df_date'])
            form_file.save()
            return JsonResponse({'status':'success','msg':'提交成功'})
        else:
            return JsonResponse({'status':'fail','msg':'提交失败'})

# 分页模型
def dis_xiaoque(request):
    #模型分页

    # 获取数据库所有数据
    xiaoque_list=AddTask.objects.all()
    # 构建分页器对象，xiaoque_list=所有数据，5=每页显示数据条数
    paginator = Paginator(xiaoque_list,5)
    # 获取具体第几页的页面对象
    page = paginator.get_page(1)
    # 数据对象总数
    count = paginator.count

    # Paginator和Page的常用API
    # page.previous_page_number()
    # page.next_page_number()
    # page.has_previous()
    # page.has_next()

    result={
        'data':['123'],
        'total':5,
        'page':page,

    }
    # pageSize = int(request.GET.get('pageSize', '5'))
    # paginator = Paginator(xiaoque_list, pageSize)
    # page = request.GET.get('page',1)
    # contacts = paginator.get_page(page)
    # data_list=[]
    # # username=contacts.user.username
    # # sender=contacts.sender.username
    # executor_list=[]
    # # for executor in contacts.executor.all():
    # # name=executor.username
    # # executor_list.append(name)
    # data=model_to_dict(contacts)
    # # data['user']=username
    # # data['sender']=sender
    # data['executor']=executor_list
    # data['send_date']=str(contacts.send_date)
    # data_list.append(data)
    # result['count']=paginator.count/pageSize
    # result['data']=data_list
    # result['page']=page
    #模型分页
    return JsonResponse({'result':result})
