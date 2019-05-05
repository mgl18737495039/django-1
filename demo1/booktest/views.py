from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect
# Create your views here.

"""视图函数"""
from .models import *
def index(request):

    return render(request,"booktest/index.html",{"raname":"a"})

def list (request):
    list1=BookInfo.objects.all()
    return render(request,"booktest/list.html",{"list1":list1})
def xiang(request,id):
    try:
        book=BookInfo.objects.get(pk=int(id))
        return render(request,"booktest/xiang.html",{'book':book})
    except:
        return HttpResponse("输入正确id")
def dele(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        list1 = BookInfo.objects.all()

        return HttpResponsePermanentRedirect( "/booktest/list", {"list1": list1})
    except:
        return HttpResponse('删除失败')