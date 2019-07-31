# coding=utf-8
import re
from django.shortcuts import render, redirect
from hashlib import sha1
from .models import *
from df_goods.models import ProductInfo
from django.http import HttpResponse, JsonResponse
from . import user_decorator


# Create your views here.

def register(request):
    return render(request, 'df_user/register.html', {'title': '用户注册'})


def register_handle(request):
    # 接收用户注册POST
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    upwd2 = post.get("cpwd")
    uemail = post.get("email")
    # 验证用户填写信息
    if not (uname and upwd and upwd2 and uemail):
        return redirect("/user/resigter")
    if len(uname) < 5 or len(uname) > 20:
        return redirect("/user/resigter")
    if re.match("^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", uemail) == None:  # re.match匹配失败时返回None
        return redirect('/user/register/')

    # 判断重命
    count = UserInfo.objects.filter(uname=uname).count()
    if count != 0:
        return redirect("/user/resigter")
    if upwd != upwd2:
        return redirect("/user/resigter")
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf-8"))
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get('uname')
    print(uname)
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


# 用户登录处理
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)

def test(request):

    return render(request, 'test.html')


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    keepsession = post.get('keepsession', 0)  # 记住账号密码

    users = UserInfo.objects.filter(uname=uname)  # 通过登录用户名查询数据库

    # 判断数据库是否存在记录，并匹配密码
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            red = redirect(url)

            if keepsession != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录-用户密码错误', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录-用户名错误', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)


@user_decorator.login
def user_center_info(request):
    user_id = request.session['user_id']
    user = UserInfo.objects.get(id=user_id)
    user_email = user.uemail
    user_name = user.uname

    # 个人中心浏览记录
    pro_ids_list = []
    pro_ids = request.COOKIES.get("pro_ids","")
    print(pro_ids)
    if pro_ids == "":
        pro_records = 0
    else:
        pro_ids_list = pro_ids.split(",")
        pro_records = []
        print(pro_ids_list)
        pro_records1 = ProductInfo.objects.get( pk = pro_ids_list[0])
        pro_records.append(pro_records1)
        if len(pro_ids_list)>1:
            pro_records2 = ProductInfo.objects.get( pk = pro_ids_list[1])
            pro_records.append(pro_records2)
        if len(pro_ids_list) > 2:
            pro_records3 = ProductInfo.objects.get( pk = pro_ids_list[2])
            pro_records.append(pro_records3)
        if len(pro_ids_list) > 3:
            pro_records4 = ProductInfo.objects.get( pk = pro_ids_list[3])
            pro_records.append(pro_records4)
        if len(pro_ids_list) > 4:
            pro_records5 = ProductInfo.objects.get( pk = pro_ids_list[4])
            pro_records.append(pro_records5)


    context = {
        'title': '个人信息',
        'user_name': user_name,
        'user_email': user_email,
        'user_page':1,
        'pro_records':pro_records

    }

    return render(request, 'df_user/user_center_info.html', context)


def user_logout(request):
    del request.session['user_name']
    del request.session['user_id']
    return redirect('/')


@user_decorator.login
def user_center_order(request):
    context = {'title': '订单中心','user_page':1}
    return render(request, 'df_user/user_center_order.html', context)


@user_decorator.login
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ureceiver = post.get('ureceiver')
        user.uaddress = post.get('uaddress')
        user.upostcode = post.get('upostcode')
        user.uphone = post.get('uphone')
    user.save()
    context = {'title': '收货地址','user':user,'user_page':1}

    return render(request, 'df_user/user_center_site.html', context)
