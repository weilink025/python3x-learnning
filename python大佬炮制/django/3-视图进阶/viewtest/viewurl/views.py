from django.shortcuts import render
from django.http import *
from django.urls import reverse
# Create your views here.
def index(request,id,pid):
    return render(request,'viewtest/index.html')
def page_not_found(request):
    return render(request, 'viewtest/404.html')
#############################################
#演示GET

def getTest1(request):
    return render(request,'viewtest/getTest1.html')

def getTest2(request):
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'viewtest/getTest2.html',context)

def getTest3(request):
    a1=request.GET.getlist('a')
    context = {'a':a1}
    return render(request,'viewtest/getTest3.html',context)

#####################################
#演示POST

def postTest1(request):#post提交
    return render(request,'viewtest/postTest1.html')

def postTest2(request):#post接收处理
    name = request.POST['uname']
    pw = request.POST['upw']
    gender = request.POST['ugender']
    hobby = request.POST.getlist('uhobby')
    context = {'name':name,'pw':pw,'gender':gender,'hobby':hobby}
    return render(request,'viewtest/postTest2.html',context)

#######################################
#演示cookies#
def cookiesTest(request):

    response = HttpResponse()
    response.delete_cookie('h1')     #删除cookies
    if 'h1' in request.COOKIES:
        response.write(request.COOKIES['h1'])     #显示cookies

    #response.set_cookie('h1','kwkw',1200)     #设置cookies

    return response


################################
#演示HttpResopnseRedirect
from django.shortcuts import redirect
def redTest1(request):
    #return HttpResponseRedirect('/redTest2/')
    return redirect('/redTest2/')   #简写
def redTest2(request):
    return HttpResponse('这是转向来的页面')


################################
#演示JsonResponse
from django.http import JsonResponse

def jsonTest(requeset):
    return JsonResponse({'list': 'abc'})


######################
#session演示#

def sessionTest1(request):  #登录
    return render(request, 'viewtest/sessionTest1.html')

def sessionTest2(request):  #接收
    request.session['uname'] = request.POST['uname']
    request.session.set_expiry(0)  #关闭浏览器就是过期
    #request.session.set_expiry(120)  #120秒没有活动则过期
    #request.session.set_expiry(timedelta(days=12))  #120秒没有活动则过期
    #request.session.set_expiry(None)   #永不过期
    request.session.set_expiry(0)  #关闭浏览器就是过期
    #return redirect('/sessionForm/')
    return redirect(reverse('viewurl:sessionForm'))  #反向解析  viewurl是 项目urls include中的namespace  sessionForm是应用app中的name

def sessionForm(request):   #展示页面
    uname=request.session.get('uname','未登录')
    context = {'uname':uname}
    return render(request,'viewtest/sessionForm.html',context)

def sessionDelete(request):           #删除session
    del request.session['uname']
    # request.session.clear()   #清空
    #request.flush()     #删除
    #return redirect('/sessionForm/')
    return redirect(reverse('viewurl:sessionForm'))    #反向解析
