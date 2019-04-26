from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from blog_1 import models

def other_blog(request,id):
    username = request.session.get("username")
    c = User.objects.get(pk=id).article_set.all()
    num=User.objects.get(pk=id).article_set.count()

    user_file = models.User_file.objects.get(user_file_id=id)
    sorts = models.Sort.objects.all()
    # 收藏

    s_username = request.session.get('username')
    s_user = User.objects.get(username=s_username)
    # 取出这个user的所有收藏记录
    article_list = []
    try:
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'other_blog.html', {'username': username, 'art': c, 'user_file': user_file,
                                                   "sorts": sorts,
                                                   'num': num, 'article_list': article_list,'id':id})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
            # 分页
        paninator = Paginator(c, 2)
        pagenum = request.GET.get("pagenum")
        if pagenum == None:
            pagenum = 1

        page = paninator.page(pagenum)
        return render(request, 'other_blog.html', {'username': username, 'art': page, 'user_file': user_file,
                                                   "sorts": sorts,
                                                   'num':num,'article_list': article_list,'id':id})