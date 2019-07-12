from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *

# Create your views here.

##新写法
def index(request):

    booklist = BookInfo.objects.all()
    context = {'title':booklist}
    return render(request,'tushu/index.html',context)

##旧写法

"""
def index(request):
    temp=loader.get_template("tushu/index.html")

    return HttpResponse(temp.render())
"""

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    Herolist=book.heroinfo_set.all()

    context = {'title':Herolist}
    return render(request, 'tushu/show.html', context)