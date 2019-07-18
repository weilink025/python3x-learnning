from django.urls import path,re_path
from  . import views

app_name = 'viewtest'   #反向解析时使用
urlpatterns = [

    ##############GET演示
    path('getTest1/',views.getTest1),#展示链接页面
    path('getTest2/',views.getTest2),#接收一键一值
    path('getTest3/',views.getTest3),#接收一键多值

##############POST演示
    path('postTest1/',views.postTest1),
    path('postTest2/',views.postTest2),
    #path('',views.index),
    #path('<int:id>',views.index),
    #re_path(r'^([0-9]+)/$',views.index),   #可以用正则表达式re_path
    #re_path(r'^(?P<id>[0-9]+)/(?P<pid>[0-9]+)/$', views.index, name='index'),  # ?P<id> 对应views接收参数是id 和 pid  如果views对应参数不正确，则会匹配不上
    #path('',views.index,name='index'),    #name='index'  给path添加名称 反向解析时使用
]



