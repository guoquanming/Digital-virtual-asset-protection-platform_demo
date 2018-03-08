from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import RecordTest

# 显示请求信息
def display_message(request):
    context = {}
    record = RecordTest.objects.all().values()
    for a in record:
        c = c + a['dataid_id'].split()
    context['ask_data'] = a
    # 把查询到的字典信息放在名为context的hello属性里
    return render(request, 'firstapp/owner_b.html', context)



# 处理请求
def review(request):
    recordid = request.POST['q']
    # 更新授权状态
    context=RecordTest.objects.values().filter(recordid=recordid)
    for i in context:
        a=str((int(i['licensetype'])+1)%2)
    context.update(licensetype=a)
    return HttpResponse('successed')
