from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

from PIL import Image
from blog_1 import models
from django.core.paginator import Paginator
def my_blog(request):
    username=request.session.get("username")
    c=User.objects.get(username=username).article_set.all()
    num=User.objects.get(username=username).article_set.count()
    id_file=User.objects.get(username=username).id
    user_file=models.User_file.objects.get(user_file_id=id_file)
    sorts = models.Sort.objects.all()

    # 分页
    paninator = Paginator(c, 2)
    pagenum = request.GET.get("pagenum")
    if pagenum == None:
        pagenum = 1

    page = paninator.page(pagenum)
    # 收藏

    # 取出这个user的所有收藏记录
    article_list = []
    try:
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'my_blog.html',
                      {'username': username, 'art': page, 'user_file': user_file, "sorts": sorts, 'num': num,
                       'article_list': len(article_list)})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
        return render(request, 'my_blog.html',
                      {'username': username, 'art': page, 'user_file': user_file, "sorts": sorts, 'num': num,
                       'article_list': len(article_list)})
def send_blog(request):
    username = request.session.get("username")
    c = User.objects.get(username=username)
    if request.method == 'GET':
        sorts = models.Sort.objects.all()
        return render(request, 'send_blog.html', {"sorts":sorts,'username':username})
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
    user_f = c.user_file
    user_f_nickname = user_f.nickname
    if request.method == 'GET':
        sorts = models.Sort.objects.all()

        return render(request, 'xiugai_user.html', {"user_f": user_f, "sorts": sorts, 'usernam': username})
    elif request.method == "POST":

        age = request.POST["age"]
        nickname = request.POST["nickname"]
        if nickname != user_f_nickname:
            try:
                user_nick = models.User_file.objects.get(nickname=nickname)
            except:

                gender = request.POST["gender"]
                hobby_user = request.POST["hobby_user"]
                pthone = request.POST["pthone"]
                speciality = request.POST["speciality"]
                Personal_quotes = request.POST["Personal_quotes"]
                try:
                    img_b = request.FILES['where']

                    img_blog = Image.open(img_b)
                    img_blog.save('./static/images/users/' + str(img_b))

                    user_f.user_img = img_b
                    user_f.age = int(age)
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
                # return HttpResponseRedirect('/my_blog/xiugai_user/',{'ero':"昵称已被占用"})
                return redirect('/my_blog/xiugai_user/', )
                # return redirect(reverse('my_blog:xiugai_user',kwargs={'ero':"昵称已被占用"}))
        else:
            gender = request.POST["gender"]
            hobby_user = request.POST["hobby_user"]
            pthone = request.POST["pthone"]
            speciality = request.POST["speciality"]
            Personal_quotes = request.POST["Personal_quotes"]
            try:
                img_b = request.FILES['where']

                img_blog = Image.open(img_b)
                img_blog.save('./static/images/users/' + str(img_b))

                user_f.user_img = img_b
                user_f.age = int(age)

                user_f.gender = gender
                user_f.hobby_user = hobby_user
                user_f.pthone = pthone
                user_f.speciality = speciality
                user_f.Personal_quotes = Personal_quotes
                user_f.save()
                return redirect('/my_blog/my_blog/')
            except:

                user_f.age = int(age)

                user_f.gender = gender
                user_f.hobby_user = hobby_user
                user_f.pthone = pthone
                user_f.speciality = speciality
                user_f.Personal_quotes = Personal_quotes
                user_f.save()
                return redirect('/my_blog/my_blog/')
def my_blogcoll(request):
    username=request.session.get("username")
    c=User.objects.get(username=username).article_set.all()
    num=User.objects.get(username=username).article_set.count()
    id_file=User.objects.get(username=username).id
    user_file=models.User_file.objects.get(user_file_id=id_file)
    sorts = models.Sort.objects.all()


    # 收藏

    # 取出这个user的所有收藏记录
    article_list = []
    article_list_2=[]
    try:
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'my_blogcoll.html',
                      {'username': username, 'art': article_list_2, 'user_file': user_file, "sorts": sorts, 'num': num,
                       'article_list': article_list})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
            article_list_2.append(list_user_coll_one.collection_article)
        # 分页
        paninator = Paginator(article_list_2, 2)
        pagenum = request.GET.get("pagenum")
        if pagenum == None:
            pagenum = 1

        page = paninator.page(pagenum)
        return render(request, 'my_blogcoll.html',
                      {'username': username, 'art': page, 'user_file': user_file, "sorts": sorts, 'num': num,
                       'article_list': article_list,'len':len(article_list)})
def quxiao(request,id):
    article_list = []

    try:
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()
    except:
        print('删除失败')
    else:
        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            if article_one==models.Article.objects.get(pk=id).article_name:
                list_user_coll_one.delete()
                return redirect(reverse('my_blog:my_blogcoll'))
