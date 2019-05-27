from . import hanzezhen
from django.conf.urls import include, url
urlpatterns = [

    url(r'^register/$',hanzezhen.register),
    url(r'^zhucechenggong/$', hanzezhen.zhucechenggong)

]