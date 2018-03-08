from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Metadata,RecordTest
from django.forms.models import model_to_dict
from django.db.models import Q
import json


# ajax后台处理
def add(request):
    # 获取前端传入的数据
    a = request.GET['a']
    b = request.GET['b']
    # 查询数据库
    search = Metadata.objects.all()

    # 按前端传入的参数a进行条件查询,contex这时是一个对象，可以直接转为字典。如果用search.value（）方法查出来的是字典，用search.value_list（）查出来的是元组。
    context=search.get(title=a)

    # 把查询到的queryset数据类型转化为字典
    cc = model_to_dict(context)

    # 把字典转化为json字符串
    bb=json.dumps(cc)

    # 返回json数据到前端
    return HttpResponse(bb)

