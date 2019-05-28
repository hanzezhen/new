from .models import student,teacher
from django.shortcuts import render
from django.http import HttpResponse
from .views import checklogin


def register(req):
    teacherlist = []
    tea=teacher.objects.all()
    for item in tea:
        teacherlist.append(item.tname)
    return render(req,'register.html',{
        'teacherlist':   teacherlist
    })



def zhucechenggong(request):
    name = request.POST.get('sname')
    sid = request.POST.get('sid')
    password = request.POST.get('password')
    teacher1 = request.POST.getlist('teacher1')
    semail = request.POST.get('semail')
    stelephone = request.POST.get('stelephone')
    tea = teacher.objects.filter(tname=teacher1[0])[0]
    st = student(sname=name, steacher=tea,semail=semail,sid=sid,stelephone=stelephone,password=password)
    st.save()
    stu=student.objects.filter(sname=name)
    return render(request,'zhucechenggong.html',{'stu':stu[0]})
