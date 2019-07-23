#coding=utf-8
import re
from django.shortcuts import render,redirect
from hashlib import sha1
from .models import *
from django.http import HttpResponse,JsonResponse
# Create your views here.

def register(request):
    return render(request,'df_user/register.html')
def register_handle(request):
    #接收用户注册POST
    post = request.POST
    uname=post.get("user_name")
    upwd=post.get("pwd" )
    upwd2=post.get("cpwd")
    uemail=post.get("email")
    #验证用户填写信息
    if not(uname and upwd and upwd2 and uemail):
        return redirect("/user/resigter")
    if len(uname)<5 or len(uname)>20:
        return redirect("/user/resigter")
    if re.match("^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", uemail) == None:  # re.match匹配失败时返回None
        return redirect('/user/register/')

    #判断重命
    count = UserInfo.objects.filter(uname=uname).count()
    if count != 0:
        return redirect("/user/resigter")
    if upwd != upwd2:
        return redirect("/user/resigter")
    #密码加密
    s1=sha1()
    s1.update(upwd.encode("utf-8"))
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    return redirect('/user/login/')

def register_exist(request):
    uname=request.GET.get('uname')
    print(uname)
    count =UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
        return render(request, 'df_user/login.html')

def login_handle(reqeust):

    pass

def user_center_info(request):
    return render(request,'df_user/user_center_info.html')

def user_center_site(request):
    return render(request,'df_user/user_center_site.html')