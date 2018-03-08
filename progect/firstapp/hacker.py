from django.shortcuts import render
from firstapp.models import Metadata,RecordTest
#黑客攻击后返回数据的下载地址
def hacker_display(request):
    ctx = {}
    c = []
    search = Metadata.objects.all().values()
    recording = RecordTest.objects.all().values()
    for record in recording:
        c = c + record['dataid_id'].split()
        ctx['hacker_data'] = search.filter(daid__in=c)
    return render(request, 'firstapp/hacker.html', ctx)
