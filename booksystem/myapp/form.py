import json
from django.http import HttpResponse,JsonResponse
import re
import datetime
from .models import student,teacher,yuyue,equipment

def ajax1get(request):
    uname = json.loads(request.body.decode())
    stu = student.objects.filter(sname=uname['username'])

    if stu :
        ret = {"sttr":"yes"}
    else:
        ret = {"sttr":"no"}
    print(ret)
    return HttpResponse(json.dumps(ret))


from .datecal import dateRange
def ajax2get(request):
    data= json.loads(request.body.decode())
    uername = data['username']
    eid =data['eid']
    val = data['val']
    now_time = datetime.datetime.now()
    datelist = dateRange(now_time)
    num = re.search(r'(^[0-9]+)and',val).group(1)
    date = datelist[int(num)-1]
    hour = re.search(r"and([0-9])$",val).group(1)
    starthour = str(int(hour)+6)+'：00'
    stu = student.objects.filter(sname=uername)[0]
    ep = equipment.objects.filter(eid=eid)[0]
    ax = yuyue.objects.filter(yeid=ep).filter(ysid=stu).filter(ydate=date).filter(ytimestart=starthour)
    if ax:
        ret = {'sttr':'no'}
    else:
        ret = {'sttr':'yes'}
        yy = yuyue(yeid=ep,ysid=stu,ydate=date,ytimestart=starthour,shichang=1.0)
        yy.save()

    print(ret)
    return HttpResponse(json.dumps(ret))


