from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    list = HeroInfo.objects.filter()
    context = {'list':list}
    return render(request,'tsapp/index.html',context)

def show(request,id):
    return render(request,'tsapp/show.html',{'id':id})
