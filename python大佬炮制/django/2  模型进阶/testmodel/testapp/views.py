from django.shortcuts import render
from . import models
# Create your views here.
def hello(request):
    bookinf = models.BookInfo.books.all()
    context = {'title':bookinf}
    return render(request,'hello.html',context)

def show(request,id):
    book = models.BookInfo.books.get(pk=id)
    heroinfo = book.heroinfo_set.all()

    context = {'title':heroinfo}
    return render(request,'show.html',context)