from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

from PIL import Image
from blog_1 import models

def my_blog(request):
    username=request.session.get("username")
    c=User.objects.get(username=username).article_set.all()
    return render(request,'my_blog.html',{'username':username,'art':c,})
def send_blog(request):
    username = request.session.get("username")
    c = User.objects.get(username=username)
    if request.method == 'GET':
        return render(request, 'send_blog.html', {})
    elif request.method == "POST":
                text_blog=request.POST["text"]
                type_blog=request.POST["type"]
                name_blog=request.POST["textname"]
                img_b=request.FILES['where']
                img_blog=Image.open(img_b)
                img_blog.save('./static/images/'+str(img_b))

                article=models.Article()
                article.article_name=name_blog
                article.article_img=img_b
                article.article_text=text_blog
                article.article_category=type_blog
                article.article_user=c
                article.save()
    return redirect('/')