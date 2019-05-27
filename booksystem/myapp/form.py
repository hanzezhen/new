import json
from .models import student
from django.http import HttpResponse,JsonResponse


def ajax1get(request):
    uname = json.loads(request.body.decode())
    stu = student.objects.filter(sname=uname['username'])

    if stu :
        ret = {"sttr":"yes"}
    else:
        ret = {"sttr":"no"}
    print(ret)
    return HttpResponse(json.dumps(ret))

def ajax2get(request):

    return HttpResponse('成功')


