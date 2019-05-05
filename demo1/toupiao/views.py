from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponsePermanentRedirect,HttpResponse
from django.db.models import F
# Create your views here.
from .models import *

def toupiao(request):
    re=Wen.objects.all()

    return render(request,'toupiao.html',{'re':re,'b':BookInfo})
def add_wen(request):
    if request.method == 'GET':
        return render(request, 'add_wen.html', {})
    elif request.method=='POST':
        wen=request.POST['wen']
        w=Wen()
        w.wen_name=wen
        w.save()
        return HttpResponseRedirect('toupiao/')
def dell(request,id):


    try:
        Wen.objects.get(pk=id).delete()
        list1 = Wen.objects.all()

        return HttpResponsePermanentRedirect("/toupiao/toupiao/", {"re": list1})
    except:
        return HttpResponse('删除失败')
def xiangqing (request,id):

    t=Wen.objects.get(pk=id).choice_wen_set.all()
    return render(request,'xiangqing.html',{'t':t,'id':id})
def add_piao(request,id):

        ch_id=request.POST['xuan']
        ch_ch=Choice_wen.objects.get(pk=ch_id)
        ch_ch.choice_num =F('choice_num')+1
        ch_ch.save()

        t = Wen.objects.get(pk=id).choice_wen_set.all()
        return render(request, 'xiangqing.html', {'t': t, 'id': id})
def add_choice(request ,id):
    if request.method=='GET':
        return render(request,'add_choice.html',{'id':id})
    elif request.method =='POST':
        cho_name=request.POST['cho']
        cho_ch=Choice_wen()
        cho_ch.choice_name=cho_name
        cho_ch.wen_choice=Wen.objects.get(pk=id)
        cho_ch.save()
        return  HttpResponseRedirect('/toupiao/xiangqing/'+str(id)+'/')
        # t = Wen.objects.get(pk=id).choice_wen_set.all()
        # return render(request, 'xiangqing.html', {'t': t, 'id': id})