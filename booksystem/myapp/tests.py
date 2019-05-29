from django.test import TestCase

# Create your tests here.
from .models import student,teacher,yuyue
from django.shortcuts import render
from django.http import HttpResponse
from .views import checklogin

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


class ep():
    def __init__(self,stu,num):
        self.yuyue = yuyue.objects.filter(ysid=stu).filter(isquxiao=False).order_by('-ydate')
        self.num =num
    def __getitem__(self, item):
        try:
            if item<self.num:
                return self.yuyue[item]
            else:return False
        except : return False

from collections import Counter


class s():
    def __init__(self,ep,num):
        self.ep = ep
        llc = equipment.objects.filter(ename=ep)[0]
        self.id = llc.eid
        if num == '1':
            self.quanxian ='1'
        else:
            self.quanxian = False
from .models import quanxian,equipment

@checklogin
def indextest(req):
    name = req.session.get('username')
    stu = student.objects.filter(sname=name)[0]
    stu1 = ep(stu, 20)
    lis = []
    for i in range(5):
        if stu1[i]:
            lis.append(stu1[i].yeid.ename)
    result = Counter(lis)
    eplist = []
    for key,value in result.items():
        if len(eplist)<5:
            eplist.append(key)
    # print('查找的最近预约设备如下：',eplist)
    eelist=[]
    for item in eplist:
        epp = equipment.objects.filter(ename=item)[0]
        if quanxian.objects.filter(qsid=stu).filter(qeid=epp):
            eelist.append('1')
        else:eelist.append('0')
    # print('查找的最近预约设备权限如下：',eelist)
    fl=[]
    for i in range(len(eelist)):
        try:
            fl.append(s(eplist[i],eelist[i]))
            # print(s(eplist[i],eelist[i]).quanxian)
        except: return None
    elist=[]
    for i in range(3):
        if stu1[i]:
            elist.append(stu1[i])
            # print(stu1[i].yeid.ename)
    # print(elist)

    name = req.session.get('username')
    stu = student.objects.filter(sname=name)[0]
    stu1 = ep2(stu)
    i = 0
    kl = []
    while type(stu1[i]) != type(1):
        # print('2',stu1[i].yeid.ename)
        kl.append(stu1[i])
        i = i + 1

    yuyuel = []
    lishil = []
    for item in kl:
        # print('e',item.yeid.ename)
        a = item.ytimestart
        # print('a', a)
        b = item.shichang
        try:
            x = re.search(r'([0-9]{2})：', a).group(1)
            xx = str(int(int(x) + b)) + 'm'
            yy = str(int(int(x) - 1))
        except:
            x = re.search(r'([0-9]{1})：', a).group(1)
            x = '0' + x
            xx = '0' + str(int(int(x) + b)) + 'm'
            yy = '0' + str(int(int(x) - 1))
        # print(yy)

        yy = re.sub(r'([0-9]{1,2})：', yy, a).replace('m', '')
        # print('try',yy)
        xx = re.sub(r'([0-9]{1,2})：', xx, a)

        xx = xx.replace('m', '：')
        item.jieshushijian = xx
        item.save()
        try:
            print(a[4])
            a = a.replace('：', '')
            # print(a)
        except:
            a = '0' + a
            a = a.replace('：', '')

        xx = xx.replace('：', '')

        # print(item.jieshushijian)
        # print(xx)
        if datetime.datetime.now().strftime("%Y-%m-%d-%H%M") < (
                item.ydate.strftime("%Y-%m-%d") + '-' + a):
            # print(item.ydate.strftime("%Y-%m-%d") + '-' +a)
            print(item.ydate.strftime("%Y-%m-%d") + '-' + a)
            print(datetime.datetime.now().strftime("%Y-%m-%d-%H%M"))
            item.qiandaoshijian = False
            if datetime.datetime.now().strftime("%Y-%m-%d-%H%M") > (
                    item.ydate.strftime("%Y-%m-%d") + '-' + yy):
                item.qiandaoshijian = True

                yuyuel.append(item)
            item.save()

            # print('当前时间',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # print('预约时间',item.ydate.strftime("%Y-%m-%d") + ' ' + item.ytimestart)
        elif datetime.datetime.now().strftime("%Y-%m-%d-%H%M") > (
                item.ydate.strftime("%Y-%m-%d") + '-' + a):
            if datetime.datetime.now().strftime("%Y-%m-%d-%H%M") < (
                    item.ydate.strftime("%Y-%m-%d") + '-' + xx):
                # print(item.yeid)
                item.qiandaoshijian = True
                item.save()
                yuyuel.append(item)

            else:
                item.qiandaoshijian = False

                lishil.append(item)
    k=len(yuyuel)
    for item in yuyuel:
        print(item.ytimestart)
    return render(req,'indextest.html',{'ep':elist,'equip':fl,'stu':stu,'kk':k})


def baseinfo(request):
    name = request.session.get('username')
    stu = student.objects.filter(sname=name)
    ep = quanxian.objects.filter(qsid=stu[0])
    st = ''
    for i in ep:
        st = st+i.qeid.ename+'|'
    print(st)
    return render(request,'baseinfo.html',{'stu':stu[0],'quanxian':st})


class ep2():
    def __init__(self,stu):
        self.yuyue = yuyue.objects.filter(ysid=stu).order_by('-ydate')
        for i in self.yuyue:
            print('1',i.yeid)
    def __getitem__(self, item):
        try:
            return self.yuyue[item]
        except : return item





@checklogin
def myappointment(request):
    name = request.session.get('username')
    stu = student.objects.filter(sname=name)[0]
    stu1 = ep2(stu)
    i=0
    kl=[]
    while type(stu1[i]) != type(1):
        # print('2',stu1[i].yeid.ename)
        kl.append(stu1[i])
        i=i+1

    yuyuel=[]
    lishil=[]
    for item in kl:
        # print('e',item.yeid.ename)
        a = item.ytimestart
        print('a',a)
        b = item.shichang
        try:
            x = re.search(r'([0-9]{2})：', a).group(1)
            xx = str(int(int(x) + b)) + 'm'
            yy = str(int(int(x) - 1))
        except:
            x = re.search(r'([0-9]{1})：', a).group(1)
            x='0'+x
            xx = '0'+str(int(int(x) + b)) + 'm'
            yy= '0'+str(int(int(x) -1))
        # print(yy)

        yy = re.sub(r'([0-9]{1,2})：', yy, a).replace('m', '')
        # print('try',yy)
        xx = re.sub(r'([0-9]{1,2})：', xx, a)


        xx = xx.replace('m', '：')
        item.jieshushijian = xx
        item.save()
        try:
            print(a[4])
            a=a.replace('：','')
            print(a)
        except:
            a='0'+a
            a=a.replace('：','')

        xx=xx.replace('：','')

        # print(item.jieshushijian)
        # print(xx)
        if datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") < (
                item.ydate.strftime("%Y-%m-%d") + '-' + a):
            # print(item.ydate.strftime("%Y-%m-%d") + '-' +a)
            item.qiandaoshijian=False
            if datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") > (
                item.ydate.strftime("%Y-%m-%d") + '-' + yy):
                item.qiandaoshijian = True
            item.save()
            yuyuel.append(item)
            # print('当前时间',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # print('预约时间',item.ydate.strftime("%Y-%m-%d") + ' ' + item.ytimestart)
        elif datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") > (
                item.ydate.strftime("%Y-%m-%d") + '-' + a):
            if datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") < (
                    item.ydate.strftime("%Y-%m-%d") + '-' + xx):
                # print(item.yeid)
                item.qiandaoshijian = True
                item.save()
                yuyuel.append(item)
            else:
                item.qiandaoshijian = False
                item.save()
                lishil.append(item)
    yuyuel.reverse()

    # print('历史预约：',lishil)
    # print('当前预约：',yuyuel)
    return render(request,'myappointment.html',{'ep1':yuyuel,'ep2':lishil,'stu':stu})

class equi_p:
    def __init__(self,stu,ep):
        a=quanxian.objects.filter(qsid=stu).filter(qeid=ep)
        print('a:',stu,ep,a)
        if a:
            self.quanxian1 = 1
        else:self.quanxian1 = 0
        self.eid=ep.eid
        self.name = ep.ename


@checklogin
def epappoint(request):
    name = request.session.get('username')
    stu = student.objects.filter(sname=name)[0]
    ep = equipment.objects.all()
    eqlist=[]
    for item in ep:
        eqlist.append(equi_p(stu,item))
    return render(request,'epappoit.html',{'equip':eqlist,'stu':stu})



import datetime
from .datecal import dateRange
import numpy as np
import re


class giveout():
    def __init__(self,matrix):
        self.matrix=matrix

    def __getitem__(self, item):
        return list(self.matrix[item,:])

@checklogin
def appoint(request,num1):
    name = request.session.get('username')
    stu = student.objects.filter(sname=name)[0]
    ep = equipment.objects.filter(eid=num1)[0]
    stimelist = list(range(7))
    rangelist = list(range(14))
    now_time = datetime.datetime.now()
    datelist = dateRange(now_time)
    yue = yuyue.objects.filter(yeid=ep).filter(isquxiao=False)
    yueli=np.zeros((24,7),dtype=object)
    kkk = 0
    for item in datelist:
        a= datetime.datetime.strptime(item, '%Y-%m-%d')
        b=yue.filter(ydate=a)
        if b:
            for ii in b:
                ts = ii.ytimestart
                try:
                    ts=ts.replace(':',"：")
                except:print('ok')
                st = r'([1-9]+)：'
                p = re.compile(st)
                sss = re.search(p, ts).group(1)
                sss = int(sss) - 1
                lll=int(ii.shichang)

                for i in range(lll):
                    yueli[sss,kkk]=ii.ysid.sname
        kkk=kkk+1
    give =giveout(yueli)
    chuandi =[]
    for gi in give:
        # print(gi)
        aa=list(gi)
        chuandi.append(aa)
    print(chuandi[7])

    if stu.isstudent == False:
        ra = 0
        for i in datelist:
            mp5 =  datetime.datetime.strptime(i,"%Y-%m-%d")
            xman = mp5.strftime('%A')

            if (xman != 'Sunday') and (xman != 'Saturday') :
                for item in chuandi:
                    item[ra] = '组外人员周内不可预约'
            ra = ra + 1

    return render(request,'appoint.html',{'t':stimelist,'s':rangelist,'date1':datelist,'epq':ep,'yueli1':chuandi[6],
                                          'yueli2': chuandi[7],'yueli3':chuandi[8],'yueli4':chuandi[9],'yueli5':chuandi[10],'yueli6':chuandi[11],'yueli7':chuandi[12],
                                          'yueli8': chuandi[13],'yueli9':chuandi[14],'yueli10':chuandi[15],'yueli11':chuandi[16],'yueli12':chuandi[17],'yueli13':chuandi[18],
                                          'yueli14': chuandi[19],'yueli15':chuandi[20],'yueli16':chuandi[21],'yueli17':chuandi[22],
                                          'eid':num1,'username':name,'stu':stu})
@checklogin
def appointfalse(request):
    return render(request,'appintfalse.html')

