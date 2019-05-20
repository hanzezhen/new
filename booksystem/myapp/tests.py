from django.test import TestCase

# Create your tests here.
from .models import student,teacher
from django.shortcuts import render
from django.http import HttpResponse

def addteacher(request):
    return render(request,'addStudents.html')


def test11(request):
    # stu = student.objects.filter(sname='111')
    # tname = request.POST.get('teachername')
    # t = teacher(tname=tname, stu=stu[0])
    # t.save()
    return HttpResponse('成功')



def index(request):
    return render(request,'index.html')

def indextest(req):
    name = req.session.get('username')
    stu = student.objects.filter(sname=name)
    class ep:
        name='1123'
        time='1'
        person='1'
        place='1'
    aep=ep()
    bep=ep()
    eplist=[aep,bep,aep]

    class equip:
        id=1
        name='某某设备'
    cequip=equip()
    dequip=equip()
    eqlist=[cequip,dequip,dequip,dequip,dequip,dequip]
    return render(req,'indextest.html',{'ep':eplist,'equip':eqlist,'stu':stu[0]})


def baseinfo(request):
    name = request.session.get('username')
    stu = student.objects.filter(sname=name)
    return render(request,'baseinfo.html',{'stu':stu[0]})

def myappointment(request):
    return render(request,'myappointment.html')
def epappoint(request):
    class equip:
        id=1
        name='某某设备'
    cequip=equip()
    dequip=equip()
    eqlist=[cequip,dequip,dequip,dequip,dequip,dequip]
    return render(request,'epappoit.html',{'equip':eqlist})



import datetime
from .datecal import dateRange
def appoint(request):
    stimelist = list(range(7))
    rangelist = list(range(14))
    now_time = datetime.datetime.now()
    datelist = dateRange(now_time)

    return render(request,'appoint.html',{'t':stimelist,'s':rangelist,'date1':datelist})

def appointfalse(request):
    return render(request,'appintfalse.html')