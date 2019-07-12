from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
# Create your views here.

##新写法
def index(request):
    return render(request,'tushu/index.html')

##旧写法

"""
def index(request):
    temp=loader.get_template("tushu/index.html")

    return HttpResponse(temp.render())
"""