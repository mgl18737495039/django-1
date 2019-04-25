import sys
sys.path.append('../')



from django.shortcuts import render,redirect,reverse
from django.db.models import Q
from django.views.decorators.http import require_GET
from django.http import HttpResponse,HttpResponsePermanentRedirect
# Create your views here.
from blog_1 import models
from django.contrib.auth.models import User


def maopao(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-i-1):
            if list1[j][1] >list1[j+1][1]:
                list1[j],list1[j+1]= list1[j+1], list1[j]
    return list1

def index(request):

    c=models .Article.objects.all()
    # 筛选出点击量前四的文档
    a = models.Article.objects.order_by('-article_click_volume')
    a_1_num=0
    a_1_list=[]
    for a_1 in a:
        a_1_list.append(a_1)
        a_1_num+=1
        if a_1_num>3:
            break
    # 筛选出时间前四的文档
    a1 = models.Article.objects.order_by('-article_time')
    a1_1_num = 0
    a1_1_list = []
    for a1_1 in a1:
        a1_1_list.append(a1_1)
        a1_1_num += 1
        if a1_1_num > 3:
            break

    # 筛选出留言前四的文档
    a2 = models.Article.objects.order_by('-article_num')
    a2_1_num = 0
    a2_1_list = []
    for a2_1 in a2:
        a2_1_list.append(a2_1)
        a2_1_num += 1
        if a2_1_num > 3:
            break

    sorts = models.Sort.objects.all()
    # 收藏


    # 取出这个user的所有收藏记录
    article_list = []
    try:
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        #该用户未收藏

        return render(request, 'one.html', {'art': c, 'art_click': a_1_list, 'art_time': a1_1_list,'art_num':a2_1_list,
                                            'username': request.session.get("username"), 'sorts': sorts, "id": id,
                                            'article_list':article_list})
    else:

        # 遍历所有的收藏记录


        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
        return render(request, 'one.html',
                      {'art': c, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, "id": id,
                       'article_list': article_list})
def fenlei(request,id):
    c=models.Sort.objects.get(id=id).article_set.all()

    # 筛选出点击量前四的文档
    a = models.Article.objects.order_by('-article_click_volume')
    a_1_num = 0
    a_1_list = []
    for a_1 in a:
        a_1_list.append(a_1)
        a_1_num += 1
        if a_1_num > 3:
            break

        # 筛选出时间前四的文档
    a1 = models.Article.objects.order_by('-article_time')
    a1_1_num = 0
    a1_1_list = []
    for a1_1 in a1:
        a1_1_list.append(a1_1)
        a1_1_num += 1
        if a1_1_num > 3:
            break

    sorts = models.Sort.objects.all()

    a2 = models.Article.objects.order_by('-article_num')
    a2_1_num = 0
    a2_1_list = []
    for a2_1 in a2:
        a2_1_list.append(a2_1)
        a2_1_num += 1
        if a2_1_num > 3:
            break

    sorts = models.Sort.objects.all()



    # 收藏



    article_list = []
    try:
        # 取出这个user的所有收藏记录
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'one.html', {'art': c, 'art_click': a_1_list, 'art_time': a1_1_list,
                                            'username': request.session.get("username"), 'sorts': sorts, "id": id,
                                            'art_num': a2_1_list,'article_list': article_list})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
        return render(request, 'one.html', {'art': c, 'art_click': a_1_list, 'art_time': a1_1_list,
                                            'username': request.session.get("username"), 'sorts': sorts, "id": id,
                                            'art_num': a2_1_list, 'article_list': article_list})
def hort_blog(request):

    # 筛选出点击量前四的文档
    a = models.Article.objects.order_by('-article_click_volume')
    a_1_num = 0
    a_1_list = []
    for a_1 in a:
        a_1_list.append(a_1)
        a_1_num += 1
        if a_1_num > 3:
            break
    # 筛选出时间前四的文档
    a1 = models.Article.objects.order_by('-article_time')
    a1_1_num = 0
    a1_1_list = []
    for a1_1 in a1:
        a1_1_list.append(a1_1)
        a1_1_num += 1
        if a1_1_num > 3:
            break

    a2 = models.Article.objects.order_by('-article_num')
    a2_1_num = 0
    a2_1_list = []
    for a2_1 in a2:
        a2_1_list.append(a2_1)
        a2_1_num += 1
        if a2_1_num > 3:
            break

    sorts = models.Sort.objects.all()


# 收藏



    article_list = []
    try:
        # 取出这个user的所有收藏记录
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'one.html',
                      {'art': a, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, 'mages': 'hort',
                       'article_list': article_list})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
        return render(request, 'one.html',
                      {'art': a, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, 'mages': 'hort',
                       'article_list': article_list})
def new_blog(request):

    # 筛选出点击量前四的文档
    a = models.Article.objects.order_by('-article_click_volume')
    a_1_num = 0
    a_1_list = []
    for a_1 in a:
        a_1_list.append(a_1)
        a_1_num += 1
        if a_1_num > 3:
            break
    # 筛选出时间前四的文档
    a1 = models.Article.objects.order_by('-article_time')
    a1_1_num = 0
    a1_1_list = []
    for a1_1 in a1:
        a1_1_list.append(a1_1)
        a1_1_num += 1
        if a1_1_num > 3:
            break

    a2 = models.Article.objects.order_by('-article_num')
    a2_1_num = 0
    a2_1_list = []
    for a2_1 in a2:
        a2_1_list.append(a2_1)
        a2_1_num += 1
        if a2_1_num > 3:
            break

    sorts = models.Sort.objects.all()


# 收藏



    article_list = []
    try:
        # 取出这个user的所有收藏记录
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'one.html',
                      {'art': a1, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, 'mages': 'new',
                       'article_list': article_list})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
        return render(request, 'one.html',
                      {'art': a1, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, 'mages': 'new',
                       'article_list': article_list})
def com_blog(request):

    # 筛选出点击量前四的文档
    a = models.Article.objects.order_by('-article_click_volume')
    a_1_num = 0
    a_1_list = []
    for a_1 in a:
        a_1_list.append(a_1)
        a_1_num += 1
        if a_1_num > 3:
            break
    # 筛选出时间前四的文档
    a1 = models.Article.objects.order_by('-article_time')
    a1_1_num = 0
    a1_1_list = []
    for a1_1 in a1:
        a1_1_list.append(a1_1)
        a1_1_num += 1
        if a1_1_num > 3:
            break

    a2 = models.Article.objects.order_by('-article_num')
    a2_1_num = 0
    a2_1_list = []
    for a2_1 in a2:
        a2_1_list.append(a2_1)
        a2_1_num += 1
        if a2_1_num > 3:
            break

    sorts = models.Sort.objects.all()


    # 收藏

    article_list = []
    try:
        # 取出这个user的所有收藏记录
        s_username = request.session.get('username')
        s_user = User.objects.get(username=s_username)
        list_user_coll = s_user.collection_set.all()

    except:
        # 该用户未收藏

        return render(request, 'one.html',
                      {'art': a2, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, 'mages': 'com' ,
                       'article_list': article_list})
    else:

        # 遍历所有的收藏记录

        for list_user_coll_one in list_user_coll:
            # 获得一条记录取出对应的文章名字
            article_one = list_user_coll_one.collection_article.article_name
            # 存入一个列表
            article_list.append(article_one)
        return render(request, 'one.html',
                      {'art': a2, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, 'mages': 'com',
                       'article_list': article_list})
def find(request):
    find_content=request.POST['find_content']
    if find_content:
        A=models.Article.objects.filter(article_name__contains=find_content)

        a = models.Article.objects.order_by('-article_click_volume')
        a_1_num = 0
        a_1_list = []
        for a_1 in a:
            a_1_list.append(a_1)
            a_1_num += 1
            if a_1_num > 3:
                break
        # 筛选出时间前四的文档
        a1 = models.Article.objects.order_by('-article_time')
        a1_1_num = 0
        a1_1_list = []
        for a1_1 in a1:
            a1_1_list.append(a1_1)
            a1_1_num += 1
            if a1_1_num > 3:
                break

        a2 = models.Article.objects.order_by('-article_num')
        a2_1_num = 0
        a2_1_list = []
        for a2_1 in a2:
            a2_1_list.append(a2_1)
            a2_1_num += 1
            if a2_1_num > 3:
                break

        sorts = models.Sort.objects.all()

        return render(request, 'find.html',
                      {'art': A, 'art_click': a_1_list, 'art_time': a1_1_list, 'art_num': a2_1_list,
                       'username': request.session.get("username"), 'sorts': sorts, })
def coll_blog(request,id):
    # 取出前端传回来的文章
    article_coll=models.Article.objects.get(pk=id)
    #取出文章的作者名字
    username=article_coll.article_user.username
    try:
        #取出session中的user
        s_username=request.session.get('username')
        s_user=User.objects.get(username=s_username)
        #取出这个user的所有收藏记录
    except:
        return redirect('/')
    else:
        try:
            list_user_coll = s_user.collection_set.all()

        except:

            if username == s_username:
                return redirect('/')
            else:
                colltion_one = models.Collection()

                colltion_one.collection_article = article_coll
                colltion_one.collection_user = s_user
                colltion_one.save()
                return redirect('/')
        else:

            #遍历所有的收藏记录
            article_list=[]

            for list_user_coll_one in list_user_coll:
                #获得一条记录取出对应的文章名字
                article_one=list_user_coll_one.collection_article.article_name
                #存入一个列表
                article_list.append(article_one)
            if username ==s_username:
                return redirect('/')
            elif article_coll.article_name in article_list:
                return redirect('/')
            else:
                colltion_one= models.Collection()

                colltion_one.collection_article=article_coll
                colltion_one.collection_user=s_user
                colltion_one.save()
                article_list.append(article_coll.article_name)
                print(article_list)
            return redirect('/')





