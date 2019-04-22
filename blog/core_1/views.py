import sys
sys.path.append('../')



from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse,HttpResponsePermanentRedirect
# Create your views here.
from blog_1 import models





def index(request):

    c=models .Article.objects.all()
    a=models .Article.objects.order_by('article_click_volume')
    a1= models .Article.objects.order_by('-article_time')


    list2=[]
    for i in models .Article.objects.all():
        b=i.comment_set.all().count()
        list2.append(b)
    list2.sort(reverse=True)


    return render(request,'one.html',{'art':c,'art_click':a ,'art_time':a1,'art_list2':list2 ,'username':request.session.get("username")})
