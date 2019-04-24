from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

from PIL import Image
from blog_1 import models

def my_blog(request):
    username=request.session.get("username")
    c=User.objects.get(username=username).article_set.all()
    id_file=User.objects.get(username=username).id
    user_file=models.User_file.objects.get(user_file_id=id_file)
    sorts = models.Sort.objects.all()
    return render(request,'my_blog.html',{'username':username,'art':c,'user_file':user_file,"sorts":sorts})
def send_blog(request):
    username = request.session.get("username")
    c = User.objects.get(username=username)
    if request.method == 'GET':
        sorts = models.Sort.objects.all()
        return render(request, 'send_blog.html', {"sorts":sorts})
    elif request.method == "POST":
                text_blog=request.POST["text"]
                type_blog=request.POST["type"]
                name_blog=request.POST["textname"]
                try:
                    img_b=request.FILES['where']

                    img_blog=Image.open(img_b)
                    img_blog.save('./static/images/'+str(img_b))

                    article=models.Article()
                    article.article_name=name_blog
                    article.article_img=img_b
                    article.article_text=text_blog

                    article.article_category=models.Sort.objects.get(sort_name=type_blog)
                    article.article_user=c
                    article.save()
                except:
                        try:
                            article = models.Article()
                            article.article_name = name_blog

                            article.article_text = text_blog
                            article.article_category = models.Sort.objects.get(sort_name=type_blog)
                            article.article_user = c
                            article.save()
                        except:
                            return redirect('/myblog/send_blog/')
    return redirect('/')
def del_blog(request,id):
    i = models.Article.objects.get(pk=id)
    for t in i.comment_set.all():
        t.delete()
    i.delete()
    return redirect('/my_blog/my_blog/')
def xiugai_user(request):
    username = request.session.get("username")
    c = User.objects.get(username=username)
    user_f=c.user_file
    if request.method == 'GET':
        sorts = models.Sort.objects.all()
        return render(request, 'xiugai_user.html', {"user_f":user_f,"sorts":sorts})
    elif request.method == "POST":

        age= request.POST["age"]
        nickname= request.POST["nickname"]
        user_nick=models.User_file.objects.get(nickname=nickname)
        if user_nick ==None:
            gender= request.POST["gender"]
            hobby_user = request.POST["hobby_user"]
            pthone = request.POST["pthone"]
            speciality = request.POST["speciality"]
            Personal_quotes = request.POST["Personal_quotes"]
            try:
                img_b = request.FILES['where']

                img_blog = Image.open(img_b)
                img_blog.save('./static/images/users/' + str(img_b))

                user_f.user_img = img_b
                user_f.age=int(age)
                user_f.nickname = nickname
                user_f.gender = gender
                user_f.hobby_user = hobby_user
                user_f.pthone = pthone
                user_f.speciality = speciality
                user_f.Personal_quotes = Personal_quotes
                user_f.save()
                return redirect('/my_blog/my_blog/')
            except:

                    user_f.age = int(age)
                    user_f.nickname = nickname
                    user_f.gender = gender
                    user_f.hobby_user = hobby_user
                    user_f.pthone = pthone
                    user_f.speciality = speciality
                    user_f.Personal_quotes = Personal_quotes
                    user_f.save()
                    return redirect('/my_blog/my_blog/')
        else:
            return HttpResponseRedirect('/my_blog/xiugai_user/',{'ero':"昵称已被占用"})
            # return redirect('/my_blog/xiugai_user/',{'ero':"昵称已被占用"})