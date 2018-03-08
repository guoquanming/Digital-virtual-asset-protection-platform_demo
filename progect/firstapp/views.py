from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Metadata,RecordTest
from django.db.models import Q
import datetime

# 首次显示：
def display_list(request):
    context = {}
    search=Metadata.objects.all()
    # 把查询到的字典信息放在名为context的hello属性里
    context['list']=search
    return render(request, 'firstapp/hello.html', context)



# 关键字搜索+分类显示
def search(request):
    ctx = {}
    key = request.POST['q']

    search = Metadata.objects.all().values().filter(title__contains=key)

    # 查出已请求数据的id
    state_already = RecordTest.objects.all().values().filter(licensetype=0)
    # 查出已请求并授权数据的id
    state_authorized = RecordTest.objects.all().values().filter(licensetype=1)

    # 查出记录表中的信息
    state_recording = RecordTest.objects.all().values()
    ctx['ask_ntyt'] = search
    if state_recording:
        # 如果记录表不为空则未申请的数据为：在metadata表中查出的数据去掉记录表中的数据id
        for recording in state_recording:
            ctx['ask_ntyt'] = ctx['ask_ntyt'].exclude(daid=recording['dataid_id'])

    # 如果记录表为空，则未申请的数据为metadata中的数据
    else:
        ctx['ask_ntyt'] = search


    # 返回已请求过的数据
    asked = {}
    c = []
    if state_already:
        for asked in state_already:
            c = c + asked['dataid_id'].split()
            ctx['ask_already'] = search.filter(daid__in=c)

    # 返回已授权的数据
    authorized = {}
    b = []
    if state_authorized:
        for authorized in state_authorized:
            # 把查找到的数据id循环出来放在列表b中
            b = b + authorized['dataid_id'].split()
            # 用in查询方法查找满足list b中的数据把查询到的多条结果直接写入字典
            ctx['authorized_already'] = search.filter(daid__in=b)
    return render(request, "firstapp/hello.html", ctx)





# 记录请求
def ask_recording(request):
    key = request.POST['q']
    record_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    authorizedperson = 'zhangsan'
    license_type = "0"
    RecordTest(
        dataid_id=key,
        recordtime=record_time,
        authorizedperson=authorizedperson,
        licensetype=license_type,
    ).save()

    return HttpResponse('successed')



