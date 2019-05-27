from django.conf.urls import include, url
from . import views,form,tests,hanzezhen_url
urlpatterns = [

    url(r'^signpass/$',views.signpass,name='signpass'),
    url(r'^foradmin/$',views.foradmin,name='formadmin'),
    url(r'^studentquanxian/$',views.studentquanxian,name='studentquanxian'),
    url(r'^studentshenqing/$',views.studentshenqing,name='studentshenqing'),
    url(r'^xiaowaishenqing/$',views.xiaowaishenqing,name='xiaowaishenqing'),
    url(r'^studentupdate/$',views.studentupdate,name='studentupdate'),
    url(r'^weekform/$',views.weekform,name='weekform'),
    url(r'^shenhe/$',views.shenhe,name='shenhe'),
    url(r'^gezhi/$',views.gezhi,name='gezhi'),
    url(r'^butongguo/$',views.butongguo,name='butongguo'),
    url(r'^dingshiforadmin/$',views.dingshiforadmin,name='dingshiforadmin'),
    url(r'^studentform/$',views.studentform,name='studentform'),
    url(r'^teacherform/$',views.teacherform,name='teacherform'),




    url(r'^login/', views.login),
    url(r'^home2/', views.home2),
    url(r'^hometrans/', views.hometrans),
    url(r'^quitlogin/', views.quitlogin),
    url(r'^(\d{3})', views.date),
    url(r'^traceback', views.traceback),
    url(r'^signup', views.signup),
    url(r'^ajax1get/', form.ajax1get),
    url(r'^test11/', tests.test11),
    url(r'^index/', tests.index),
    url(r'^indextest/', tests.indextest),
    url(r'^baseinfo/', tests.baseinfo),
    url(r'^myappointment/', tests.myappointment),
    url(r'^epappoint/', tests.epappoint),
    url(r'^appoint(\d{1,3})/', tests.appoint),
    url(r'^appointfalse/', tests.appointfalse),

    url(r"^",include('myapp.hanzezhen_url',namespace='myapp1'))
]
