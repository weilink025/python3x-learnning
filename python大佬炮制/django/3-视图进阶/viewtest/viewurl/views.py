from django.shortcuts import render

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
